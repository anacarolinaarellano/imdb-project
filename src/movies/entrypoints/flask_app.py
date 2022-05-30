from flask import Flask, render_template, request
from movies import models
import pandas as pd
import os

#Use Template
app = Flask(__name__, template_folder='templates')
models.start_mappers()

# Get path to list (one directory up)
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
pathTotmp = os.path.abspath(os.path.join(__location__ ,".."))

@app.route("/hello", methods=["GET"])
def hello_world():
    return "Hello World!!!", 200

@app.route("/movie-list", methods=["GET"])
def movie_list():
    data = pd.read_csv(pathTotmp+'/movie_results.csv')
    order = request.args.get('order')
    if order=='desc':
        data = data.sort_values(by='preference_key', ascending=False)
    if order=='asc':
        data = data.sort_values(by='preference_key', ascending=True)
    return render_template('table.html', tables=[data.to_html()], titles=[''])