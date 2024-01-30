from flask import Flask, render_template, flash, request

app = Flask(__name__)
app.secret_key = "hussain"

data = [
        {"name":"hussain", "age":23, "address": "kadapa"},
        {"name":"valli", "age":24, "address": "hyd"},
        {"name":"anil", "age":25, "address": "bangalore"}
    ]

@app.route('/')
def index():
    return render_template("index.html", data=data)

# @app.route('/tasks/<int:task_id>', methods=['GET'])
@app.route('/delete_data/', methods =["GET", "POST"])
def delete_data():
    name = request.form.get('t1')
    print("Name...........", name)
    res = [ data.pop(index) for index, dt in enumerate(data) if dt['name'] == name]
    flash(f"{name} has been deleted")
    return render_template('index.html', data=data)                                                                                                            
    

####################################################################
## Some crud apis 
from flask import Flask, request, jsonify


# Sample data for demonstration
tasks = [
    {
        'id': 1,
        'title': 'Task 1',
        'description': 'Description 1',
        'done': False
    },
    {
        'id': 2,
        'title': 'Task 2',
        'description': 'Description 2',
        'done': False
    }
]

# CRUD operations

# Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Get a specific task by ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify({'task': task})

# Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        return jsonify({'error': 'Title is required'}), 400

    task = {
        'id': tasks[-1]['id'] + 1 if tasks else 1,
        'title': request.json['title'],
        'description': request.json.get('description', ''),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

# Update a task by ID
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404

    task['title'] = request.json.get('title', task['title'])
    task['description'] = request.json.get('description', task['description'])
    task['done'] = request.json.get('done', task['done'])

    return jsonify({'task': task})

# Delete a task by ID
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'result': True})



if __name__ == "__main__":
    app.run(debug=True)