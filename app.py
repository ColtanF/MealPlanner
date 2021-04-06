#! python
from flask import Flask, render_template, flash, redirect, url_for, request
from wtforms import Form, StringField, TextAreaField, IntegerField, validators

app = Flask(__name__)
app.debug = True

class Recipe():
    def __init__(self, name, ingr, cals, recipe):
        self.name = name
        self.ingr = ingr
        self.cals = cals
        self.recipe = recipe
meals = {}
meals["Pizza"] = Recipe("Pizza", "Dough, Cheese, Sauce", "1000", "Make dough, put sauce and cheese on, bake at 400 degrees for 10 minutes.")
meals["Chicken and Broccoli"] = Recipe("Chicken and Broccoli", "Chicken Breast, Broccoli", "400", "Cook chicken breast in air fryer at 375 degrees for 17 minutes, flipping once halfway through the cooking time. Steam broccoli.")

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
    return render_template('meal.html', meal=id, ingredients=meals[id].ingr)

class RecipeForm(Form):
    recipeName = StringField('Recipe Name', [validators.Length(min=1, max=200)])
    ingredients = TextAreaField('Ingredients', [validators.Length(min=5)])
    calories = IntegerField('Calories', [validators.NumberRange(min=0)])
    recipe = TextAreaField('Recipe', [validators.Length(min=30)])


@app.route('/add_meal', methods=["GET", "POST"])
def add_meal():
    form = RecipeForm(request.form)
    if request.method == "POST" and form.validate():
        recipeName = form.recipeName.data
        ingredients = form.ingredients.data
        calories = form.calories.data
        recipe = form.recipe.data

        meals[recipeName] = Recipe(recipeName, ingredients, calories, recipe)
        flash("Meal Added!", "success")
        return redirect(url_for("browse"))

    return render_template('add_meal.html', form=form)

if __name__ == "__main__":
    app.secret_key = 'secret123'
    app.run(port=5002)