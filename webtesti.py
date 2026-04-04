from flask import Flask,render_template, request
import json
import sqlite3

app = Flask(__name__)
@app.route('/save', methods=['POST'])
def memory():
    connect=sqlite3.connect('document.db')
    cursor=connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS memory (text TEXT)")
    data=cursor.fetchall()
    write_text=request.form.get('user_text')
    connect=sqlite3.connect('document.db')
    cursor=connect.cursor()
    cursor.execute(f"INSERT INTO memory (text) VALUES(?)", (write_text,))
    connect.commit()
    connect.close()
    return render_template('thanks.html')

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/thanks')
def show_thanks():
    return  render_template('thanks.html')
if __name__ =='__main__':
    app.run(debug=True)
