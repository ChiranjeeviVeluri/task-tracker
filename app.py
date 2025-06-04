from flask import Flask, request, jsonify


app = Flask(__name__)


# In-memory list to store tasks
# app.py


# Initial hard-coded tasks (converted from JSON to Python):
tasks = []



@app.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify(tasks), 200


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json or {}
    title = data.get("title", "").strip()
    if not title:
        return jsonify({"error": "Title is required"}), 400

    task = {"id": len(tasks) + 1, "title": title}
    tasks.append(task)
    return jsonify(task), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
