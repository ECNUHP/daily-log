#正则表达式的替换和使用
import re

#sentence = "2004-959-559 # (swe)个国外电话号《》码"
def reprocess(sentence):
    pattern1= re.compile(r'《[、.。！!,，？?""“”～()（） \d a-zA-Z]*》')
    pattern2=re.compile(r'\([、.。！!,，？?""“”～\d a-zA-Z ]*\)')
    pattern3=re.compile(r'（[、.。！!,，？?""“”～\d a-zA-Z ]*）')
    list1=re.findall(pattern1, sentence)
    list2=re.findall(pattern2,sentence)
    list3=re.findall(pattern3,sentence)
    list1.extend(list2)
    list1.extend(list3)
    for i in list1:
        sentence=sentence.replace(i,'')
    return sentence


#提取连续的数字
    import re
    number_pattern = re.compile('\d+')



	
#函数用于删掉字符串中所有的空白字符
def delete_space(str):
    import re
    pattern = re.compile(r'\s')
    list= re.findall(pattern, str)
    for c in list :
        str = str.replace(c, '')
    return str
	
	
	
#跑程序log 记录
from log import Logger

log = Logger('./run_log/train.log',level='info')

log.logger.info("Created trec_lda_model with fresh parameters.")

#删除列表重复元素，不改变列表元素顺序

m = ['b','c','d','b','c','a','a']
n = sorted(set(m),key=m.index)

#结巴分词，带词性识别
import jieba.posseg as pseg

seg=pseg.cut( line.strip())
for ele in seg :
	if ele.word in ciku_dict or ele.flag in tag_list:
	...
	

#统计列表中有多少个不同的元素
import numpy as np
list=[1,2,3,4,3,4,5,1]
l=len(np.unique(list))



#两个列表同时打乱，相对位置保持不变
from sklearn.utils import shuffle

x=[1,2,3]
y=[4,5,6]
x,y=shuffle(x,y)

def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False

def check_chinese_str(content):
    for char in content:
        if not  is_chinese(char):
            return False
    return True

列表：

0第一个元素，-1最后一个元素，


-len第一个元 素，len-1最后一个元素

import os

eword_list=[]
rootdir = r'C:\Users\hp\Desktop\情感词语'
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
for i in range(0,len(list)):
    path = os.path.join(rootdir,list[i])
    with open(path,'r',encoding='utf-8')as infile:

#列表去重并按照原始列表的顺序排列
list1 = ['是恶疾','但是','但是','可是','但是']
list2 = list(set(list1))

print(list2)
list2.sort(key = list1.index)
print(list2)	




#多个对象利用字典捆绑，方便处理
with open('./seg/all_message.txt', 'r', encoding='utf-8') as f:
    post = [line.strip() for line in f.readlines()]
with open('./seg/all_response.txt', 'r', encoding='utf-8') as f:
    response = [line.strip() for line in f.readlines()]
with open('./seg/keywords.txt', 'r', encoding='utf-8') as f:
    keyword = [line.strip() for line in f.readlines()]

with open('./seg/post_topic_words.txt', 'r', encoding='utf-8') as f:
    post_topic_words = [line.strip() for line in f.readlines()]
with open('./seg/emotion_label.txt', 'r', encoding='utf-8') as f:
    emotion_label = [line.strip() for line in f.readlines()]


data = []
for p, r, k,pt,el in zip(post, response, keyword,post_topic_words,emotion_label):
    data.append({'post': p, 'response': r, 'keyword': k,'post_topic_words':pt,'emotion_label':el})

#对列表元素逆置
word_list=['1','2','3']
word_list=list(reversed(word_list))




命令行解析模块：

import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--ground_truth',default='test_target.txt',help="ground truth text file, one example per line")
    parser.add_argument('--predicted',default='res.txt' ,help="predicted text file, one example per line")
    parser.add_argument('--embeddings',default='w2v.pkl' ,help="embeddings bin file")
    args = parser.parse_args()
	
    w2v_file=open(args.embeddings,'rb')




#
dropout=(0 if numLayers==1 else dropout)

#print 不换行输出
print (x,end = '')  不换行输出


读取并且遍历csv文件
import pandas as pd
pd_all = pd.read_csv( r'C:\Users\hp\Desktop\FQA\financezhidao_filter.csv',header=0)

for idx,item in pd_all.iterrows():
	
#numpy
x[:,n]表示在全部数组（维）中取第n个数据，直观来说，x[:,n]就是取所有集合的第n个数据, 即取出第n列数据
x[n,:]表示在n个数组（维）中取全部数据，直观来说，x[n,:]就是取第n集合的所有数据, 即取出第n行数据


if else 简写：
idList = self.trainIdList if type=='train' else self.testIdList


#batch_generator


def batch_generator(data, batch_size, shuffle=False):
    data_size=len(data)
    if shuffle:
        import random
        random.shuffle(data)
    if data_size<=batch_size:
        return [data]
    else:
        batch_list=[]
        batch_count = int(data_size /batch_size)+1
        for i in range(batch_count):
            start=i*batch_size
            end=start+batch_size
            if start<data_size:
                batch_list.append(data[start:end])
        return batch_list

x=[1,12,2,3,4,5]
for e in batch_generator(x,batch_size=4):
    print(e)



写入csv文件和xlsx文件的方法

import pandas as pd
result_list = []
with open('test.txt','r',encoding='utf-8')as infile:
    for line in infile:
        line_list=line.strip().split('\t')
        line_list[2]=int(line_list[2])
        result_list.append(line_list)

columns = ["sentence1", "sentence2", "label"]
dt = pd.DataFrame(result_list, columns=columns)
dt.to_excel("result_xlsx.xlsx", index=0)
dt.to_csv("test.csv", index=0)


#python操作excel文件.

import xlrd
workbook1 = xlrd.open_workbook(r'C:\Users\User\Desktop\20191203-对练系统-多意图识别\node.xlsx')
sheet1=workbook1.sheet_by_name('Sheet1')
scenery_dict={}

for row in range(sheet1.nrows):
    if row ==0 or row==7:
        continue
    key=sheet1.cell_value(row,0)
    value=sheet1.cell_value(row,3)
    scenery_dict[key]=value


#在py文件中要导入上级目录下的文件，需要将路径加载进来

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))


#把分好词的长文本序列按照标点符号划分成句子列表

def split_chinese_sentence(text):
    """
    Segment a input Chinese text into a list of sentences.
    :param text: a segmented input string.
    :return: a list of segmented sentences.
    """
    if type(text) == list:  # already segmented
        words = text
    else:
        words = str(text).split()
    start = 0
    i = 0
    sents = []
    punt_list = '。!！?？;；~～'
    for word in words:
        word = word
        token = list(words[start:i + 2]).pop()
        if word in punt_list and token not in punt_list:
            sents.append(words[start:i + 1])
            start = i + 1
            i += 1
        else:
            i += 1
            token = list(words[start:i + 2]).pop()

    if start < len(words):
        sents.append(words[start:])


    sents = [" ".join(x) for x in sents]
    return sents

text='你好 今天 我 是 。 但是 你 知道吗 ？ 我 不知道 。'
print(split_chinese_sentence(text))




当py文件下有相对路径的时候,为了方便其他文件调用，路径这样写不会有找不到路径的问题
os.path.join(os.path.dirname(__file__),'model/esim_48.ckpt')


# 利用正则匹配找到字字符串的位置：

import re


def get_match_spans(pattern, input):
    """
    Given string pattern and string input,
    return list of [) char position tuples of patterns in input.
    :param pattern: string pattern to match.
    :param input: string input where we find pattern.
    :return: a list of pattern char position tuples in input.
    """
    spans = []
    for match in re.finditer(re.escape(pattern), input):
        spans.append(match.span())
    return spans


if __name__ == "__main__":
    # test get_match_spans
    pattern = "are"
    input = "how are you are you"
    print(get_match_spans(pattern, input))
    # we will get [(4, 7), (12, 15)]

============================================================================

#计算编辑距离：


def minDistance( word1: str, word2: str) -> int:
    n1 = len(word1)
    n2 = len(word2)
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    # 第一行
    for j in range(1, n2 + 1):
        dp[0][j] = dp[0][j-1] + 1
    # 第一列
    for i in range(1, n1 + 1):
        dp[i][0] = dp[i-1][0] + 1
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] ) + 1
    #print(dp)
    return dp[-1][-1]


#四舍五入保留四位小数
res=0.8
res=('%.4f'%res)
print(res)



#利用def clean_sentence(text):
    text = re.sub(r"[^A-Za-z0-9^,?!.\/'+=]", " ", text)
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"can't", "cannot ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r",", " , ", text)
    text = re.sub(r"\.", " . ", text)
    text = re.sub(r"!", " ! ", text)
    text = re.sub(r"\?", " ? ", text)
    text = re.sub(r"\/", " ", text)
    text = re.sub(r"\^", " ^ ", text)
    text = re.sub(r"\+", " + ", text)
    text = re.sub(r"\-", " - ", text)
    text = re.sub(r"\=", " = ", text)
    text = re.sub(r"'", " ", text)
    text = re.sub(r":", " : ", text)
    text = re.sub(r"\s+", " ", text)

    return text


text="what's the weather like ? what's "
print(clean_sentence(text))正则表达式，替换字符

获取当前文件路径，可根据嵌套的深度不端添加 os.path.dirname
os.path.dirname(os.path.abspath(__file__))


