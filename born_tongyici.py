import os
import jieba
import jieba.analyse
import jieba.posseg as pseg
from cilin import CilinSimilarity
from openpyxl import workbook

f = open('./static/词组.txt')
word_list = []

wb = workbook.Workbook()
ws = wb.active
ws.append(['单词'])

for each_line in f :
    #print(each_line)
    each_line = each_line.replace('/','').replace('、','').replace('（','').replace('）','').split('\n')#去掉每行末尾的换行符
    cut_words = jieba.lcut(each_line[0],cut_all=False)#.cut()返回生成器，.lcut()返回列表。
    #print(cut_words)
tongyici = CilinSimilarity()
    #tongyi_words = tongyici.return_tongyici(cut_words[0])#实例化cilin中的类
    #print(tongyi_words)