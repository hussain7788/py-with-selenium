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

@app.route('/delete_data/', methods =["GET", "POST"])
def delete_data():
    name = request.form.get('t1')
    print("Name...........", name)
    res = [ data.pop(index) for index, dt in enumerate(data) if dt['name'] == name]
    flash(f"{name} has been deleted")
    return render_template('index.html', data=data)                                                                                                            
    
    


if __name__ == "__main__":
    app.run(debug=True)