import jieba
from search import find_node_from_rela


def knife(word):
    words = jieba.cut(word,cut_all=False)
    print(list(words))
    for i in words:



print(knife('固定太阳能'))