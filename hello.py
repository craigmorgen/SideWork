from flask import Flask, jsonify, request, g
import sqlite3


app = Flask(__name__)


conn = sqlite3.connect('TheBats.db')
c = conn.cursor()


@app.route('/')
def hey_there():
    return 'Who are you? I\'m Batman'


@app.route('/message')
def get_message():
    conn = sqlite3.connect('TheBats.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM batquote')
    entries = cur.fetchall()
    return jsonify(entries)


@app.route('/message/new', methods=['POST'])
def post_message():
    batquote = request.json['message']
    conn = sqlite3.connect('TheBats.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO batquote (message) VALUES(?)', (batquote,))
    conn.commit()
    return cur.lastrowid


@app.route('/message/<int>')
def get_messageID():
    return jsonify(placeholder2)


if __name__ == '__main__':
    app.run(debug=True, port=8080)