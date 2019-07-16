from flask import Flask, request
from flask import render_template
import pymssql
from flask_bootstrap import Bootstrap
import jieba

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/', methods=['POST', 'GET'])
def index():
    querywords = request.form.get('query')
    if querywords is not None:









        conn = pymssql.connect('localhost','sa', '123', 'CreapDBsong')  # 本机地址、用户名、密码、所用数据库名称
        cur = conn.cursor()
        sql = "SELECT [id] ,[functionName]  FROM [CreapDBsong].[dbo].[Functions] \
        WHERE [functionName] = '{}'" .format(querywords)  # 此处的{}外面必须加引号，否则报错
        cur.execute(sql)
        u = cur.fetchone()  # 获得该功能的id
        print(u)
        print(u[0])
        sql2 = " SELECT [Effect_id] FROM [CreapDBsong].[dbo].[FunctionEffects]\
        where Function_id = '{}'".format(u[0])
        cur.execute(sql2)
        u2 = cur.fetchall()  # 获得该功能对应的所有的效应id，以列表返回

        print(u2)
        effect = []
        for i in u2:  # 依次获得所有效应的名称、内容，以列表返回
            print(i[0])
            sql3 = " SELECT [effectName],[effectContent] FROM [CreapDBsong].[dbo].[Effects] where id = '{}'".format(i[0])
            cur.execute(sql3)
            u = cur.fetchone()
            effect.append([u[0], u[1]])
        conn.close()
        print(effect)
        return render_template('function.html', u=effect)
    return render_template('index.html')


if __name__ == '__main__':

    app.run(debug=True )


