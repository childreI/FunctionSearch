# -*- coding: utf-8 -*-
import os
import jieba
import jieba.analyse
import jieba.posseg as pseg


def gen_stop_words():
    #获得停用词表
    with open('stopword.txt', 'r', encoding='utf-8') as fp:
        stop_words = [_.strip() for _ in fp.readlines()]
    return stop_words


def text_seg(text: str, stop_words: list = None) -> list:
    #对输入的文本利用jieba分词进行分词
    seg_list = []
    if not stop_words:
        stop_words = gen_stop_words()
    for word, flag in pseg.cut(text):
        if word not in stop_words and not word.isspace():
            # 对于单词 全部默认小写
            seg_list.append({word.lower():flag})
    return seg_list

print(text_seg('分解垃圾'))