import sqlite3
import json
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/api/whiskey', methods=['GET', 'POST'])
def collection():
    if request.method == 'GET':
        all_whiskey = get_all_whiskey()
        return json.dumps(all_whiskey)
    elif request.method == 'POST':
            data = request.form
            result = add_whiskey(data['name'], data['abv'], data['price'])
            return jsonify(result)

def get_all_whiskey():
    with sqlite3.connect('whiskey.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM whiskey ORDER BY id desc")
        all_whiskey = cursor.fetchall()
        return all_whiskey

@app.route('/api/whiskey/<whiskey_id>', methods=['GET', 'PUT', 'DELETE'])
def resource(whiskey_id):
    if request.method == 'GET':
        whiskey = get_single_whiskey(whiskey_id)
        return json.dumps(whiskey)
    elif request.method == 'PUT':
        data = request.form
        result = edit_whiskey(
            whiskey_id, data['name'], data['abv'], data['price'])
        return jsonify(result)
    elif request.method == 'DELETE':
        result = delete_whiskey(whiskey_id)
        return jsonify(result)

def get_single_whiskey(whiskey_id):
    with sqlite3.connect('whiskey.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM whiskey WHERE id = ?", (whiskey_id,))
        whiskey = cursor.fetchone()
        return whiskey

def add_whiskey(name, abv, price):
    try:
        with sqlite3.connect('whiskey.db') as connection:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO whiskey (name, abv, price) values (?, ?, ?);
                """, (name, abv, price,))
            result = {'status': 1, 'message': 'Whiskey Added'}
    except:
        result = {'status': 0, 'message': 'error'}
    return result

def edit_whiskey(whiskey_id, name, abv, price):
    try:
        with sqlite3.connect('whiskey.db') as connection:
            connection.execute("UPDATE whiskey SET name = ?, abv = ?, price = ? WHERE ID = ?;", (name, abv, price, whiskey_id,))
            result = {'status': 1, 'message': 'WHISKEY Edited'}
    except:
        result = {'status': 0, 'message': 'Error'}
    return result

def delete_whiskey(whiskey_id):
    try:
        with sqlite3.connect('whiskey.db') as connection:
            connection.execute("DELETE FROM whiskey WHERE ID = ?;", (whiskey_id,))
            result = {'status': 1, 'message': 'WHISKEY Deleted'}
    except:
        result = {'status': 0, 'message': 'Error'}
    return result

if __name__ == '__main__':
    app.debug = True
    app.run()
