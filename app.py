import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGODB_NAME"] = os.environ.get("MONGODB_NAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/breakfast_recipes")
def breakfast_recipes():
    all_recipes = mongo.db.recipes.find()
    return render_template("breakfast_recipes.html",
    recipes=all_recipes)

@app.route("/main_recipes")
def main_recipes():
    all_recipes = mongo.db.recipes.find()
    return render_template("main_recipes.html",
    recipes=all_recipes)

@app.route("/dessert_recipes")
def dessert_recipes():
    all_recipes = mongo.db.recipes.find()
    return render_template("dessert_recipes.html",
    recipes=all_recipes)

@app.route("/view_recipe/<recipe_id>")
def view_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("view_recipe.html", recipe=the_recipe)

@app.route("/add_recipes")
def add_recipes():
    all_categories = mongo.db.categories.find()
    return render_template("add_recipes.html",
    categories=all_categories)

@app.route("/insert_recipe", methods=["POST"])
def insert_recipe():
    recipes = mongo.db.recipes

    form_data = request.form.to_dict()

    ingredients_list = form_data["ingredients"].split("\n")
    instructions_list = form_data["instructions"].split("\n")

    recipes.insert_one(
        {
        "category_name": form_data["category_name"],
        "recipe_name": form_data["recipe_name"],
        "image_link": form_data["image_link"],
        "ingredients": ingredients_list,
        "instructions": instructions_list
        }
    )

    return redirect(url_for("thank_you_add"))

@app.route("/thank_you_add")
def thank_you_add():
    return render_template("thank_you_add.html")

@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    ingredients_list = [ingredient for ingredient in the_recipe['ingredients']]
    instructions_list = [instruction for instruction in the_recipe['instructions']]

    ingredients_text = "\n".join(ingredients_list)
    instructions_text = "\n".join(instructions_list)

    return render_template("edit_recipe.html", recipe=the_recipe, categories=all_categories, ingredients=ingredients_text, instructions=instructions_text)

@app.route("/update_recipe/<recipe_id>", methods=["POST"])
def update_recipe(recipe_id):
    recipe = mongo.db.recipes

    form_data = request.form.to_dict()

    ingredients_list = form_data["ingredients"].split("\n")
    instructions_list = form_data["instructions"].split("\n")

    recipe.update( {"_id": ObjectId(recipe_id)},
        {
        "category_name": form_data["category_name"],
        "recipe_name": form_data["recipe_name"],
        "image_link": form_data["image_link"],
        "ingredients": ingredients_list,
        "instructions": instructions_list
        }
    )
    
    return redirect(url_for("thank_you_edit"))

@app.route("/thank_you_edit/<category>")
def thank_you_edit(category):
    return render_template("thank_you_edit.html", category=category)

@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)
