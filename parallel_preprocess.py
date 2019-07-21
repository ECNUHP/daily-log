import json
import warnings
warnings.filterwarnings('ignore')
from gensim.models.coherencemodel import CoherenceModel
import nltk.stem as ns
import nltk.tokenize as tk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize, pos_tag

import os

# nltk.download()
# tokens = tk.word_tokenize(words)
lemmatizer = ns.WordNetLemmatizer()
wnl = WordNetLemmatizer()

#构建停用词表
stop_words=[]
with open('stopwords.txt','r',encoding='utf-8')as outfile:
    for word in outfile.readlines():
        stop_words.append(word.strip())

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None


def word_lemmatize(tokens):
    """
    将
    args
        tokens: 词列表
    return
        lemmas_sent: 词列表

    """
    lemmas_sent = []
    tagged_sent = []
    for token in tokens:
        tagged_sent.extend(pos_tag([token]))    # 获取单词词性

    for tag in tagged_sent:
        wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
        lemmas_sent.append(wnl.lemmatize(tag[0], pos=wordnet_pos)) # 词形还原

    return lemmas_sent

def check_english(en_str):

    return en_str.isalpha()

def preprocess(sentence):
    #sentence 是一个原始的句子
    #return 返回一个处理好的词语列表
    #先对句子分词
    word_list0=word_tokenize(sentence)
    #词语还原
    temp=[]
    for word in word_list0:
        if word.endswith('\\n'):
            word = word[:len(word) - 2]
        if word !='':
            temp.append(word)

    word_list1=word_lemmatize(temp)
    #print(word_list1)
    #去除停用词和不是英文的词汇
    word_list2=[]
    for w in word_list1:
        if w.lower() not in stop_words and check_english(w):
            word_list2.append(w)
    return word_list2



#from multiprocessing import Pool
import multiprocessing as mp
import math



#path=r'full_marco_sessions_ann_split-train.txt'
#path='mini_train.txt'
outfile=open('parall_full_train.txt','w',encoding='utf-8')

def p_line(lines,return_dict,i):

    temp_list=[]
    for line in lines:
        line_list = line.strip().split('\t')
        line = line_list[2]
        line = ' '.join(preprocess(line))
        temp_list.append(line)

    return_dict[i]=temp_list


if __name__ == "__main__":
    import time
    import numpy as np
    start_time=time.time()

    print('CPU的个数是：{}'.format(os.cpu_count()))
    path=r'/gpfs/home/lianghe/huopei/SentenceEmotion/Trec/full_marco_sessions_ann_split-train.txt'
    with open(path,'r',encoding='utf-8')as infile:
        manager=mp.Manager()
        return_dict=manager.dict()
        lines=infile.readlines()
        p_num=os.cpu_count()
        #数据分割
        split_lines= np.array_split(lines, p_num)
        print(len(split_lines))
        process_list=[]
        #创建多个进程处理数据
        for i in range(p_num):
            p=mp.Process(target=p_line, args=(split_lines[i],return_dict,i))
            print('process {} start'.format(i))
            p.start()
            process_list.append(p)
        #等待所有的子进程都结束了，然后开始执行父进程
        [ap.join() for ap in process_list]


    for line_list in return_dict.values():
        for line in line_list:
            #print(line)
            outfile.writelines(line+'\n')

    end_time=time.time()
    print('程序执行时间：'+str(end_time-start_time)+'s')








