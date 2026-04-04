from flask import Flask,render_template
import json
import sqlite3

app = Flask(__name__)
@app.route('/save', methods=['POST'])
def memory():
    connect=sqlite3.connect('document.db')
    cursor=connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS memory (text TEXT)")
    data=cursor.fetchall()

def save_data():
    write_text=request.form.get('user_text')
    connect=sqlite3.connect('document.db')
    cursor=connect.cursor()
    cursor.execute("INSERT INTO memory (text) VALUES(?)", (write_text))
    connect.commit()
    comnect.close()
    return f"save {write_text}"

@app.route('/')
def home():
    return  render_template('index.html')
if __name__ =='__main__':
    memory()
    app.run(debug=True)
