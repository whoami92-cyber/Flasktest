from flask import Flask,render_template
import json
import sqlite3

app = Flask(__name__)

def memory():
    contnrct=sqlite3.contect('documemt.db')
    cursor=conect.cursor()
    cursor.ececute("SELECT * FROM  memory")
    data=cursor.fetchall()
    conect.close()
    return data

@app.route('/')
def home():
    return  render_template('index.html')
if __name__ =='__main__':
    app.run(debug=True)
