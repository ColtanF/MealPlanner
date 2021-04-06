#! python
from flask import Flask, render_template, flash, redirect, url_for, request
from wtforms import Form, StringField, TextAreaField, IntegerField, validators
from flask_mysqldb import MySQL

app = Flask(__name__)
app.debug = True

class Recipe():
    def __init__(self, name, ingr, cals, recipe):
        self.name = name
        self.ingr = ingr
        self.cals = cals
        self.recipe = recipe

# Configure Flask app with MySql
# Note: to get this site up and running, the developer must do the following:
# - Install MySQL
# - Create a DB called mealplanner_db
# - Create a table called meals (more later on)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'qwerQWER1234!@#$' # Change this to something actually secure
app.config['MYSQL_DB'] = 'mealplanner_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/browse')
def browse():
    # Create cursor
    cur = mysql.connection.cursor()

    # Get meals
    result = cur.execute("SELECT * FROM meals")

    meals = cur.fetchall()

    return render_template('browse.html', meals=meals)
    
@app.route('/browse/<string:id>/')
def meal(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Get meals
    result = cur.execute("SELECT * FROM meals WHERE id = %s", (id))

    meal = cur.fetchone()

    return render_template('meal.html', meal=meal)

class RecipeForm(Form):
    recipeName = StringField('Recipe Name', [validators.Length(min=1, max=200)])
    ingredients = TextAreaField('Ingredients', [validators.Length(min=5)])
    servingsPerMeal = IntegerField('Number of servings', [validators.NumberRange(min=0)])
    servingSize = StringField('Serving Size', [validators.Length(min=1)])
    calories = IntegerField('Calories per serving', [validators.NumberRange(min=0)])
    recipe = TextAreaField('Recipe', [validators.Length(min=30)])


@app.route('/add_meal', methods=["GET", "POST"])
def add_meal():
    form = RecipeForm(request.form)
    if request.method == "POST" and form.validate():
        recipeName = form.recipeName.data
        ingredients = form.ingredients.data
        servingsPerMeal = form.servingsPerMeal.data
        servingSize = form.servingSize.data
        calories = form.calories.data
        recipe = form.recipe.data

        # Create cursor
        cur = mysql.connection.cursor()

        # Execute SQL command - Insert meal into db
        cur.execute("INSERT INTO meals(recipeName, ingredients, servingsPerMeal, servingSize, calories, recipe) VALUES(%s, %s, %s, %s, %s, %s)", (recipeName, ingredients, servingsPerMeal, servingSize, calories, recipe))

        # Commit to db
        mysql.connection.commit()

        # Close the connection
        cur.close()

        flash("Meal Added!", "success")
        return redirect(url_for("browse"))

    return render_template('add_meal.html', form=form)

if __name__ == "__main__":
    app.secret_key = 'secret123' # Again, change this to something secure or hide it in an .env file
    app.run(port=5002)