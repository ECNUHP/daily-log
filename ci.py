
from flask import Flask, request, g, jsonify
import argparse
import os
import json
import pandas as pd
import logging
import time
import traceback
from predict import ClassfierPredictor
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
app = Flask(__name__)





HOST = "0.0.0.0"
PORT = 7784
DEBUG = True


time_str = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
if DEBUG:
    logging.basicConfig(level=logging.INFO)

else:
    logging.basicConfig(level=logging.INFO,
                    filename='output/ci/export/log/{}.log'.format(time_str),
                    )


def before_request():
    global predictor
    logging.info("load classfication model start !")
    ##init intention classification model
    predictor = ClassfierPredictor(args.model_path, args.label2id_path, args.vocab_path, args.max_seq_length)
    ## load node2labels
    global node2lables
    node2lables = load_node2lables(args.node2labels)
    logging.info("load classfication model end !")

@app.route("/")
def index():
    """Retrieve information about the deployed model."""
    global predictor
    res = {
        "input": "json", ## {data: {"context": "xxxxxxxxxxxx", "question": "xxxxxxxxx", "unique_id"="xxx"}
        "output": "json"
    }
    return jsonify(res)


@app.route('/parse', methods=['GET', 'POST'])
def predict():
    global predictor
    if request.method == 'POST':
        slim = str(request.form.get("slim"))
        input = request.form.get('question')
        model_id = request.form.get('model_id')
        result = {}
        result["result0"] = []
        result["result1"] = []
        try:
            res0, res1 = run_ci(input, predictor, node2lables, model_id, slim)
        except slimError as e:
            logging.info(e.message)
            result["code"] = e.code
            result = json.dumps(result, ensure_ascii=False)
            return result
        except modelidError as e:
            logging.info(e.message)
            result["code"] = e.code
            result = json.dumps(result, ensure_ascii=False)
            return result
        except Exception as e:
            logging.info("Classification model occur an error.")
            logging.info(repr(e))
            logging.info(traceback.format_exc())
            result["code"] = 300
            result = json.dumps(result, ensure_ascii=False)
            return result
        result["code"] = 0
        result["result0"] = res0
        result["result1"] = res1
        result = json.dumps(result, ensure_ascii=False)
        logging.info("Successs: %s" % input)
        return result
    else:
        slim = str(request.args.get("slim"))
        input = request.args.get('question')
        model_id = request.args.get('model_id')
        result = {}
        result["result0"] = []
        result["result1"] = []
        try:
            res0, res1 = run_ci(input, predictor, node2lables, model_id, slim)
        except slimError as e:
            logging.info(e.message)
            result["code"] = e.code
            result = json.dumps(result, ensure_ascii=False)
            return result
        except modelidError as e:
            logging.info(e.message)
            result["code"] = e.code
            result = json.dumps(result, ensure_ascii=False)
            return result
        except Exception as e:
            logging.info(e)
            logging.info("Classification model occur an error.")
            logging.info(e)
            result["code"] = 300
            result = json.dumps(result, ensure_ascii=False)
            return result
        result["code"] = 0
        result["result0"] = res0
        result["result1"] = res1
        result = json.dumps(result, ensure_ascii=False)
        logging.info("Successs: %s" % input)
        return result


class Node:
    def __init__(self, name, id, mode_id, intentions):
        self.name = name
        self.id = id
        self.mode_id = mode_id
        self.intentions = intentions


class MyException(Exception):

    def __init__(self, *args):
        self.args = args


class slimError(MyException):
    def __init__(self, code=100, message='Parameter slim error.'):
        self.message = message
        self.code = code

class modelidError(MyException):
    def __init__(self, code=200, message='Parameter id error.'):
        self.message = message
        self.code = code

def load_node2lables(path):
    node2labels = {}
    pd_data = pd.read_excel(path, sheetname="Sheet1")
    for index, row in pd_data.iterrows():
        node2labels[row["模型id"]] = Node(row["节点名"], row["节点id"], row["模型id"], list(str(row["子意图"]).split()))
    return node2labels



def split_sentences(text, slim):
    if slim == "0":
        puncs = ['？', '。', '！']
    elif slim == "1":
        puncs = ['？', '。', '！', '，']
    else:
        raise slimError()
    sents = []
    last_index = 0
    for i, ch in enumerate(text):
        if i == len(text)-1:
            sents.append(text[last_index: i+1])
            break
        if ch in puncs:
            sents.append(text[last_index: i+1])
            last_index = i + 1
    return sents


def normalization(data):
    new_data = []
    sum = 0.
    for d in data:
        sum += d[1]
    for d in data:
        new_data.append([d[0], d[1]/sum])
    return new_data

def run_ci(input, predictor, node2lables, node, slim):


    ## segment sentences
    sents = split_sentences(input, slim)
    ## add total sentence in tail
    sents.append(input)

    norm_results = []
    results = predictor.predict(sents)
    if node not in node2lables:
        raise modelidError()
    node_lables = node2lables[node].intentions
    for res in results:
        new_res = []
        for r in res:
            label = r[0].replace("__label__", "")
            if label in node_lables:
                new_res.append([label, r[1]])
        new_res = normalization(new_res)
        norm_results.append(new_res)
    norm_results = norm_results[0:-1]
    last_result = norm_results[-1]
    result0 = [
        {
            "text": sents[-1],
            "label": last_result[0][0],
            "confidence": last_result[0][1]
        }
    ]
    result1 = []
    for s, n_r in zip(sents, norm_results):
        res_json = {
            "text": s,
            "label": n_r[0][0],
            "confidence": n_r[0][1]
        }
        result1.append(res_json)


    return result0, result1





if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", default="./output/ci/export/1575406343", help="model file path")
    parser.add_argument("--vocab_path", default="./output/ci/export/vocab.txt", help="vocab file path")
    parser.add_argument("--max_seq_length", default=128,
                        help="The maximum total input sequence length after WordPiece tokenization. "
                             "Sequences longer than this will be truncated, and sequences shorter "
                             "than this will be padded.")
    parser.add_argument("--label2id_path", default="./output/ci/export/label2id.json",
                        help="the path of label2id.json file ")
    parser.add_argument("--node2labels", default="./output/ci/export/node.xlsx",
                        help="the path of node.xlsx file ")
    args = parser.parse_args()
    before_request()
    app.run(host=HOST, port=PORT, debug=DEBUG)



    # # text = "王小姐，您好！这里是招商银行信用卡中心，我姓X，工号是TA002，很高兴为您服务，您现在通话方便吗？"
    #
    # text = "礼品抢兑的活动一会儿会给您发短信，您跟着上面的提示操作就行了。现在您可以选择抢兑拉杆箱或者2019个积分，活动是秒杀的方式，先到先得，抢完完成为止，每个月只能成功抢兑一次。还有，额外赠送的388积分，也不要忘了在掌上生活领取，积分到账后有效期是一年。我再强调一下哦，稍后您会接收到一条短信，跟着短信最后的操作就可以了。本次活动您可以选择法国进口品牌ELLE品牌的拉杆箱或者2019个积分，是二选一的，先到先得，抢完为止，活动当月仅限成功抢兑一次， 388积分要到掌上生活领取，积分有效期一年。重要的事情说三遍：活动的参与方法我一会儿会给您发送短信，现在可以抢兑两种礼品，拉杆箱或者是2019个积分，礼品是抢完为止，每个月只能成功抢兑一次，另外送您的388积分也请在掌上生活领取，有效期是一年。"
    # text = "礼品抢兑的活动一会儿会给您发短信，您跟着上面的提示操作就行了。现在您可以选择抢兑拉杆箱或者2019个积分，活动是秒杀的方式，先到先得，抢完为止，每个月只能成功抢兑一次。还有，额外赠送的388积分，也不要忘了在掌上生活领取，积分到账后有效期是一年。"
    #
    # node = "成交确认4"
    #
    # run_ci(text, node)

    #
    # text = "刘先生你好，我这里是招商银行中心的"
    # node = "明确身份"
    # run_ci(text, node)




