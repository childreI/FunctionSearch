from py2neo import Graph,Node,walk,Relationship,NodeSelector
graph=Graph("http://localhost:7474", username="neo4j", password="123456")


# 查询node
def find_node(graph,node_name,output=None):
    s=NodeSelector(graph)
    try:
        if(output):
            return output(s.select(name=node_name).first())
        else:
            return s.select(name=node_name).first()
    except:
        return '没有这个'+node_name+'节点，查询失败'


#print(find_node(graph,'稳住',dict))


# 查询与节点有特定关系的节点

def find_node_from_rela(graph , node_name ,relationship):
    node =find_node(graph ,node_name)
    tmp =[]
    try:
        for n in graph.match(start_node=node ,rel_type=relationship):
            tmp.append(n.end_node()["name"])
        for n in graph.match(end_node=node,rel_type=relationship):
            tmp.append(n.start_node()["name"])
        return tmp[-1]
    except:
        return '输入有误，查询失败'


#print(find_node_from_rela(graph ,'固定' ,'相似'))
#print(find_node_from_rela(graph ,'太阳能' ,'相似'))

# 查询两个节点的关系
def find_rela(graph, node_name_1, node_name_2):
    node_1 = find_node(graph, node_name_1)
    node_2 = find_node(graph, node_name_2)
    try:
        rel = graph.match_one(start_node=node_1, end_node=node_2)
        return node_name_1 + rel.type() + node_name_2
    except:
        try:
            rel = graph.match_one(start_node=node_2, end_node=node_1)
            return node_name_2 + rel.type() + node_name_1
        except:
            return node_name_1 + '与' + node_name_2 + '没有关系'





