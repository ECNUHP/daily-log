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