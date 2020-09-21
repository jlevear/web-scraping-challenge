from flask import Flask, render_template, jsonify, redirect, url_for
from flask_pymongo import PyMongo

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

from scrape_mars import scrape

# Create an instance of our Flask app.
app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_data = mongo.db.collection.find_one()
    print(mars_data.keys())
    return render_template('index.html', mars=mars_data)

@app.route("/scrape")
def find_data():

    new_data = scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, new_data, upsert=True)

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)