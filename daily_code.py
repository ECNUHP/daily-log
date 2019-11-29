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















