import sqlite3
from flask_restful import Api, Resource, reqparse

class Note(Resource):
    def get(self, id=0):
        conn = sqlite3.connect('notes.db')
        c = conn.cursor()
        if id == 0:
            c.execute('SELECT * FROM notepad')
            return c.fetchall(), 200
        t = (id,)
        c.execute('SELECT * FROM notepad WHERE id=?', t)
        results = c.fetchone()
        if results:
            conn.commit()
            return results, 200
        return "id not found", 404

    def post(self):
        conn = sqlite3.connect('notes.db')
        c = conn.cursor()
        parser = reqparse.RequestParser()
        parser.add_argument("note")
        params = parser.parse_args()

        new = (params["note"],)
        c.execute("INSERT INTO notepad(note) VALUES(?)", new)
        conn.commit()
        return new, 201

    def put(self, id):
        conn = sqlite3.connect('notes.db')
        c = conn.cursor()
        parser = reqparse.RequestParser()
        parser.add_argument("note")
        params = parser.parse_args()

        new = (id, params["note"],)

        c.execute("REPLACE INTO notepad(id,note) VALUES(?,?)",(new))
        conn.commit()
        return new, 200

    def delete(self, id):
        conn = sqlite3.connect('notes.db')
        c = conn.cursor()
        t = (id,)
        c.execute('DELETE FROM notepad WHERE id=?', t)
        conn.commit()
        return f"Note with id {id} is deleted", 200