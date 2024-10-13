from flask import Flask, render_template
from pymongo import MongoClient
# Creates the application instance
app = Flask(__name__)

# Creates the Mongodb Client
mongodb_client = MongoClient("mongodb+srv://c0922588:euNDPkwaoqrP4WSV@assignment2.78inc.mongodb.net/?retryWrites=true&w=majority&appName=Assignment2")

db = mongodb_client.shop_db
products_collection = db.products

products = [
    {
      "name": "Laptop",
      "tag": "Electronics",
      "price": 899.99,
      "image_path": "images/laptop.jpg"
    },
    {
      "name": "Coffee Mug",
      "tag": "Kitchenware",
      "price": 12.99,
      "image_path": "images/mug.jpg"
    },
    {
      "name": "Headphones",
      "tag": "Electronics",
      "price": 199.99,
      "image_path": "images/headphones.jpg"
    }
]
# products_collection.insert_many(products)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/products")
def products():
    products = list(products_collection.find())
    return render_template("product.html", products=products)

app.run(host="0.0.0.0", port=5000)