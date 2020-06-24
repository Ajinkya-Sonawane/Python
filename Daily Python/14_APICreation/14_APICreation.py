from flask import Flask, jsonify
import mysql.connector

mydb = None
def createConnection():
    global mydb
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="YOUR_MYSQL_USERNAME",
        passwd="YOUR_MYSQL_PASSWORD",
        database="dailypy"
    )
    print(mydb)

def get_articles(keyword=''):
    cursor = mydb.cursor()
    cursor.execute("Select * from articles where name like '%"+keyword+"%'")
    articles = cursor.fetchall()
    jsonResult = []
    for article in articles:
        jsonResult.append({
            'ArticleName':article[0],
            'ArticleLink':article[1]
        })
    return jsonResult

createConnection()
from pprint import PrettyPrint  er
pp = PrettyPrinter()    
pp.pprint(get_articles())

app = Flask(__name__)

@app.route('/')
def pageLoad():
    return jsonify({"Welcome Message " :"Hello There, visit 127.0.0.1:1234/articles"})

@app.route('/articles')
def loadAllArticles():
    response = get_articles()
    if len(response) == 0:
        return jsonify({"Error":"Sorry could not find any articles"})
    else:
        return jsonify(response)

@app.route('/articles/<keyword>')
def loadArticlesByKeyword(keyword):
    response = get_articles(keyword)
    print(response)
    if len(response) == 0:
        return jsonify({"Error":"Sorry could not find any articles with keyword "+keyword})
    else:
        return jsonify(response)


if __name__ == '__main__':
    app.run(port=1234,debug=True)

