# import necessary libraries
from flask import Flask, jsonify
from flask_pymongo import PyMongo

# create instance of Flask app
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/project2"

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app)


@app.route("/")
def home():
    return (
        f"<p>Welcome to Project 2's APIs!</p>"
        f"<p>Usage:</p>"
        f"/api/v1.0/HSGrads"
    )

# /api/v1.0/HSGrads
# Query for the High School graduates by state for 2009-2016
# Returns the JSON representation of the dictionary.
@app.route("/api/v1.0/HSGrads")
def HS_Grads_by_state():
    hs_results = list(mongo.db.HS_graduates_by_state.find({}, {'_id': False}))

    cur = mongo.db.HS_graduates_by_state.find()

    return jsonify(hs_results)

if __name__ == "__main__":
    app.run(debug=True)