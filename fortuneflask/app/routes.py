from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/two', methods =["GET","POST"])
def two():
    userdata = dict(request.form)
    name = userdata["fullname"]
    print(userdata)
    print(name)
    return render_template("two.html", name=name)

@app.route('/final', methods= ["get", "post"])
def final():
    userdata = dict(request.form)
    number = userdata["number"]
    print(userdata)
    number = int(number)
    print(number)
    output = model.fortuneteller(number)
    print(output)
    return output
