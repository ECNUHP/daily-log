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











