from py2neo import Node ,Graph,Relationship
import pandas as pd
g=Graph("http://localhost:7474/",
    username="neo4j",
    password="123456")
g.delete_all()

word_data = pd.read_excel('./static/tongyiciaaa.xlsx',encoding="gbk",header=0)

for i in range(0,len(word_data)):
    temp = Node('word', name=str(word_data['name'][i]))
    g.create(temp)
print(len(word_data))

data=pd.read_csv('./static/tongyici.csv', header=0, sep=',')
print (len(data))
for m in range(0,len(data)):
    try:
        rel = Relationship(g.find_one(label='word', property_key='name', property_value=data['name'][m]), data['guanxi'][m], g.find_one(label='word', property_key='name', property_value=data['name2'][m]))
        g.create(rel)
    except AttributeError:
        print(m)


