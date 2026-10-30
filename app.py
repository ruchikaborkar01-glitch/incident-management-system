import sqlite3
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
DB = "incidents.db"

def db():
    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row
    return c

def init():
    with db() as c:
        c.execute("""CREATE TABLE IF NOT EXISTS incidents(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL, description TEXT,
            severity TEXT DEFAULT 'medium',
            status TEXT DEFAULT 'open',
            assigned_to TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP)""")

@app.route("/")
def home():
    return render_template("index.html")

@app.get("/api/incidents")
def list_incidents():
    with db() as c:
        rows = c.execute("SELECT * FROM incidents ORDER BY id DESC").fetchall()
    return jsonify([dict(r) for r in rows])

@app.post("/api/incidents")
def create_incident():
    d = request.get_json()
    with db() as c:
        cur = c.execute(
            "INSERT INTO incidents(title,description,severity) VALUES(?,?,?)",
            (d["title"], d.get("description", ""), d.get("severity", "medium")))
    return jsonify({"id": cur.lastrowid}), 201

@app.put("/api/incidents/<int:i>")
def update_incident(i):
    d = request.get_json()
    with db() as c:
        c.execute("""UPDATE incidents SET
            assigned_to=COALESCE(?,assigned_to),
            status=COALESCE(?,status) WHERE id=?""",
            (d.get("assigned_to"), d.get("status"), i))
    return jsonify({"ok": True})

@app.post("/api/incidents/<int:i>/resolve")
def resolve_incident(i):
    with db() as c:
        c.execute("UPDATE incidents SET status='resolved' WHERE id=?", (i,))
    return jsonify({"ok": True})

init()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
