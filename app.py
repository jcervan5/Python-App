import sqlite3
from flask import Flask


app = Flask(__name__)


@app.route('/api/whiskey', methods=['GET', 'POST'])
def collection():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
            data = request.form
            result = add_whiskey(data['name'], data['abv'], data['price'])
            return jsonify(result)



@app.route('/api/whiskey/<whiskey_id>', methods=['GET', 'PUT', 'DELETE'])
def resource(whiskey_id):
    if request.method == 'GET':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass

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

if __name__ == '__main__':
    app.debug = True
    app.run()
