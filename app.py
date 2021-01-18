from flask import Flask
from flask_restful import Api
import sqlite3
from models import Note

app = Flask(__name__)
api = Api(app)

conn = sqlite3.connect('notes.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS notepad
             (id integer PRIMARY KEY, note text)''')

api.add_resource(Note, "/notes-list", "/notes-list/", "/notes-list/<int:id>")

if __name__ == '__main__':
    app.run(debug=True)