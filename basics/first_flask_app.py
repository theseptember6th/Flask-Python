"""
AUTHOR:KRISTAL SHRESTHA
DATE:6/22/2024
PURPOSE:creating first flask app
"""
from flask import Flask

app = Flask(__name__)
print(type(app))
print(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/kristal")
def hello_kristal():
    return "<p>Hello, Kristal bhai2!</p>"

app.run(debug=True)