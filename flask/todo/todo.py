from flask import Flask, render_template, request, redirect
import peewee as pw

db = pw.PostgresqlDatabase("todo_list")

class Todo(pw.Model):
    task = pw.CharField(null=False)
    
    class Meta:
        database = db

db.connect()
db.create_tables([Todo])

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    todos =Todo.select()
    return render_template("index.html", todos=todos)

@app.route('/', methods=["POST"])
def add_todo():
    print()
    print(request.form)
    print()
    task = request.form["task"]
    Todo.create(task=task)
    return redirect('/')

app.run(debug=True)