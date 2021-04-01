#! python
from flask import Flask, render_template, flash, redirect, url_for, request

app = Flask(__name__)
app.debug = True

meals = {}
meals["Pizza"] = ["Dough", "Sauce", "Cheese"]
meals["Chicken and Broccoli"] = ["Chicken", "Broccoli"]

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/browse')
def browse():

    return render_template('browse.html', meals=meals)
    
@app.route('/browse/<string:id>/')
def meal(id):
    return render_template('meal.html', meal=id, ingredients=meals[id])

if __name__ == "__main__":
    #app.secret_key = 'secret123'
    app.run(port=5002)