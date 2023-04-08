from flask import Flask, redirect, render_template, url_for, request, flash, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context().push()

app.config['SECRET_KEY'] = "hussain"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.sqlite3'

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    completed = db.Column(db.Boolean, default = False)
    created = db.Column(db.DateTime)

    def __repr__(self) -> str:
        return self.title
    

@app.route('/', methods= ['GET', 'POST'])
def index():

    if request.method == "POST":
        print("post methood is invoked")
        title = request.form.get('t1')
        comp = request.form.get('t2')
        
        if comp == "on":
            comp = True
        else:
            comp = False
        obj = Todo(title= title, completed= comp)
        db.session.add(obj)
        db.session.commit()
        print("title::", title, "comp::", comp)
        flash("Task is added")
        return redirect('/')
    
    result = Todo.query.all()
    context = {"data": result}
    return render_template("index.html", **context)

@app.route('/update/<int:id>', methods= ['GET', 'POST'])
def update_todo(id):
    
    return f"this is update todo{id}"

@app.route('/delete/<int:id>', methods= ['GET', 'POST'])
def delete_todo(id):
    res = Todo.query.get(id)

    db.session.delete(res)
    db.session.commit()
    flash("Task is Deleted")

    return redirect('/')
    
if __name__ == '__main__':
    app.run(debug= True)