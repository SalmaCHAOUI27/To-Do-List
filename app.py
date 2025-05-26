from flask import Flask, render_template, request, jsonify
from database import init_db, add_task, get_tasks, delete_task

app = Flask(__name__)

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def tasks():
    tasks = get_tasks()
    return jsonify(tasks)

@app.route('/add-task', methods=['POST'])
def add():
    data = request.get_json()
    task = data.get('task')
    date = data.get('date')
    add_task(task, date)
    return jsonify({'status': 'success'})

@app.route('/delete-task/<int:task_id>', methods=['DELETE'])
def delete(task_id):
    delete_task(task_id)
    return jsonify({'status': 'deleted'})

if __name__ == '__main__':
    app.run(debug=True)
