"""
AUTHOR:KRISTAL SHRESTHA
DATE:6/22/2024
PURPOSE:creating first flask app
"""
from flask import Flask,render_template

app = Flask(__name__)
print(type(app))
print(app)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/about")
def hello_kristal():
    name="kristal"
    return render_template('about.html',name2=name)

app.run(debug=True)