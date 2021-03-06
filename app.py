import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# DB URI import for local workspace
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGODB_NAME"] = os.environ.get("MONGODB_NAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

# Route to index page


@app.route("/")
def home():
    return render_template("index.html", page_title="Home")


# Route to view_recipe_category page, providing data for all recipes in DB
@app.route("/view_recipe_category/<selected_category>")
def view_recipe_category(selected_category):
    all_recipes = mongo.db.recipes.find()
    return render_template("view_recipe_category.html",
                           recipes=all_recipes,
                           selected_category=selected_category,
                           page_title=selected_category + "Recipes")


# Route to view_recipe page, providing data for the selected recipe
@app.route("/view_recipe/<recipe_id>")
def view_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("view_recipe.html",
                           recipe=the_recipe,
                           page_title="View Recipe")


# Route to add_recipe page, providing data for population of category formfield
@app.route("/add_recipes")
def add_recipes():
    all_categories = mongo.db.categories.find()
    return render_template("add_recipe.html",
                           categories=all_categories,
                           page_title="Add Your Own Recipe")


# Inserts the new recipe into the database with user inputs
@app.route("/insert_recipe", methods=["POST"])
def insert_recipe():
    recipes = mongo.db.recipes

    form_data = request.form.to_dict()

    ingredients_list = form_data["ingredients"].split("\n")
    instructions_list = form_data["instructions"].split("\n")

    the_recipe = recipes.insert_one(
        {
         "category_name": form_data["category_name"],
         "recipe_name": form_data["recipe_name"],
         "image_link": form_data["image_link"],
         "description": form_data["description"],
         "ingredients": ingredients_list,
         "instructions": instructions_list
        }
    )

    return redirect(url_for("view_recipe",
                            recipe_id=the_recipe.inserted_id))


# Route to edit_recipe page, providing data for population of formfield values
@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    ingredients_list = [ingredient for ingredient
                        in the_recipe['ingredients']]
    instructions_list = [instruction for instruction
                         in the_recipe['instructions']]

    ingredients_text = "\n".join(ingredients_list)
    instructions_text = "\n".join(instructions_list)

    return render_template("edit_recipe.html",
                           recipe=the_recipe,
                           categories=all_categories,
                           ingredients=ingredients_text,
                           instructions=instructions_text,
                           page_title="Edit Recipe")


# Updates the recipe in the database with user changes
@app.route("/update_recipe/<recipe_id>", methods=["POST"])
def update_recipe(recipe_id):
    recipe = mongo.db.recipes

    form_data = request.form.to_dict()

    ingredients_list = form_data["ingredients"].split("\n")
    instructions_list = form_data["instructions"].split("\n")

    recipe.update({"_id": ObjectId(recipe_id)},
                  {
                   "category_name": form_data["category_name"],
                   "recipe_name": form_data["recipe_name"],
                   "image_link": form_data["image_link"],
                   "description": form_data["description"],
                   "ingredients": ingredients_list,
                   "instructions": instructions_list
                   })

    return redirect(url_for("view_recipe",
                            recipe_id=recipe_id))


# Deletes the selected recipe from database
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP", "0.0.0.0"),
            port=int(os.environ.get("PORT", 5000)),
            debug=False)
