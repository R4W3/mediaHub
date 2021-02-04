from flask import Flask, render_template, redirect, request, session
from flask_compress import Compress
import mysql.connector
import requests

app = Flask(__name__)
app.secret_key = "dfsgjl646385sädjkgjhhöalosdhhtas"
Compress(app)

@app.route("/")
def homepage():

    return render_template("/index/index.html")

if __name__ == "__main__":
    app.run(host='localhost', port=5001, debug=True)