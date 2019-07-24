import jieba
from search import find_node_from_rela, find_node
from py2neo import Graph,Node,walk,Relationship,NodeSelector

graph = Graph("http://localhost:7474/", username="neo4j", password="123456")


def turn(word):
    words = list(jieba.cut(word,cut_all=False))
    print(words)
    m = ''
    for i in words:
        n = find_node_from_rela(graph,'{}'.format(i),'相似')
        m = m + n
    return m

