#import dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
#import the solution in python
import scrape_mars

#create instance of Flask
app = Flask(__name__)


mongo = PyMongo(app)

# create route that renders index.html
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data_dict = scrape_mars.scrape()
    mars.update(
        {},
        mars_data_dict,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
