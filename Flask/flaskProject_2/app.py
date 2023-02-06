from flask import Flask
from flask import redirect, url_for, render_template, request
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///test.db'
# with app.app_context():
#     db = SQLAlchemy(app)

# class TestDB(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(200), nullable=False)

#     def __repr__(self) -> str:
#         return self.id
app = Flask(__name__)

@app.route('/admin')
def admin_page():
    return f"this is admin page"

@app.route('/staff')
def staff_page():
    return f"this is staff page"

@app.route('/student')
def student_page():
    return f"this is student page"

# pass parameters to url like below
@app.route('/user/<name>')
def user(name):
    if name== "admin":
        return redirect(url_for('admin_page'))
    
    if name== "staff":
        return redirect(url_for('staff_page'))
    
    if name== "student":
        return redirect(url_for('student_page'))

# add_url_rule function uses
# add_url_rule func takes params as rule= actual endpoint, endpoint=we can use none, function=function to navigate
app.add_url_rule('/valli', None, admin_page)

@app.route('/')
def Message():
    return render_template('admin_login.html')

@app.route('/validate_admin', methods=['POST'])
def validate_admin():
    # return render_template('validate_admin.html')
    user = request.form.get('user')
    password = request.form.get('pass')
    
    if user== "hussain" and password == "hussain":
        return render_template("admin_welcome.html", name=user)
    else:
        error_msg = {"error": f"{user} is invalid"}
        return render_template("admin_login.html", message=error_msg)

if __name__ == '__main__':
    app.run(debug=True)

