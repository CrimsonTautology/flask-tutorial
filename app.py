from flask import Flask
import json
import mysql.connector

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Docker!'


@app.route('/widgets')
def get_widgets():
    mydb = mysql.connector.connect(
        host='mysqldb',
        user='root',
        password='p@ssw0rd1',  # this is only a demo
        database='inventory'
    )

    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM widgets')

    row_headers = [d[0] for d in cursor.description]

    results = cursor.fetchall()
    json_data = []

    for result in results:
        json_data.append(dict(zip(row_headers, result)))

    cursor.close()

    return json.dumps(json_data)


@app.route('/db')
def db_init():
    # obviously not secure
    mydb = mysql.connector.connect(
        host='mysqldb',
        user='root',
        password='p@ssw0rd1',
    )
    cursor = mydb.cursor()

    cursor.execute('DROP DATABASE IF EXISTS inventory')
    cursor.execute('CREATE DATABASE inventory')
    cursor.close()

    mydb = mysql.connector.connect(
        host='mysqldb',
        user='root',
        password='p@ssw0rd1',
        database='inventory'
    )
    cursor = mydb.cursor()

    cursor.execute()
    cursor.execute('DROP TABLE IF EXISTS widgets')
    cursor.execute(
        'CREATE TABLE widgets (name VARCHAR(255), description VARCHAR(255))'
    )
    cursor.close()

    return 'init database'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
