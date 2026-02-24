
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = "database.db"


def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    data = request.get_json()
    titulo = data.get("titulo")
    descricao = data.get("descricao")

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tarefas (titulo, descricao) VALUES (?, ?)", (titulo, descricao))
    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Tarefa criada com sucesso"}), 201


@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    conn.close()

    lista = []
    for tarefa in tarefas:
        lista.append({
            "id": tarefa[0],
            "titulo": tarefa[1],
            "descricao": tarefa[2]
        })

    return jsonify(lista)


@app.route("/tarefas/<int:id>", methods=["PUT"])
def atualizar_tarefa(id):
    data = request.get_json()
    titulo = data.get("titulo")
    descricao = data.get("descricao")

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("UPDATE tarefas SET titulo = ?, descricao = ? WHERE id = ?", (titulo, descricao, id))
    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Tarefa atualizada com sucesso"})


@app.route("/tarefas/<int:id>", methods=["DELETE"])
def deletar_tarefa(id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Tarefa deletada com sucesso"})


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
