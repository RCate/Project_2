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
        f"<h1>Welcome to Project 2's APIs!</h1>"
        f"<p>Usage:</p>"
        f"<p>/api/v1.0/HSGrads</p>"
        f"<p>/api/v1.0/PctChangeEnrollment2Yr</p>"
        f"<p>/api/v1.0/PctChangeEnrollment4Yr</p>"
        f"<p>/api/v1.0/BachelorsDegrees</p>"
        f"<p>/api/v1.0/NonBachelorsDegrees</p>"
        f"<p>/api/v1.0/Tuition2Year</p>"
        f"<p>/api/v1.0/Tuition4Year</p>"
    )

# /api/v1.0/HSGrads
# Query for the High School graduates by state for 2009-2016
# Returns the JSON representation of the dictionary.
@app.route("/api/v1.0/HSGrads")
def HS_Grads_by_state():
    hs_results = list(mongo.db.HS_graduates_by_state.find({}, {'_id': False}))
    return jsonify(hs_results)

# /api/v1.0/PctChangeEnrollment2Yr
# Query for the percent change enrollment in 2-year institutions by state for 2002-2015
# Returns the JSON representation of the dictionary.
@app.route("/api/v1.0/PctChangeEnrollment2Yr")
def Enroll_2yr_by_state():
    enroll_2yr_results = list(mongo.db.pct_chg_enroll_2year_by_state.find({}, {'_id': False}))
    return jsonify(enroll_2yr_results)

# /api/v1.0/PctChangeEnrollment4Yr
# Query for the percent change enrollment in 4-year universities by state for 2002-2015
# Returns the JSON representation of the dictionary.
@app.route("/api/v1.0/PctChangeEnrollment4Yr")
def Enroll_4yr_by_state():
    enroll_4yr_results = list(mongo.db.pct_chg_enroll_4year_by_state.find({}, {'_id': False}))
    return jsonify(enroll_4yr_results)

# /api/v1.0/BachelorsDegrees
# Query for the Bachelor's Degrees awarded for 2003-2015
# Returns the JSON representation of the dictionary.
@app.route("/api/v1.0/BachelorsDegrees")
def Bach_degrees_by_year():
    bach_results = list(mongo.db.bachelors_degrees_by_year.find({}, {'_id': False}))
    return jsonify(bach_results)

# /api/v1.0/NonBachelorsDegrees
# Query for the Non-Bachelor's Degrees awarded for 2003-2015
# Returns the JSON representation of the dictionary.
@app.route("/api/v1.0/NonBachelorsDegrees")
def Non_bach_degrees_by_year():
    non_bach_results = list(mongo.db.non_bachelors_degrees_by_year.find({}, {'_id': False}))
    return jsonify(non_bach_results)

# /api/v1.0/Tuition2Year
# Query for the tuition cost for 2-year institutions by state for 2004-2018
# Returns the JSON representation of the dictionary.
@app.route("/api/v1.0/Tuition2Year")
def Tuition2Year_by_state():
    tuition2Year_results = list(mongo.db.tuition_2year_by_state.find({}, {'_id': False}))
    return jsonify(tuition2Year_results)

# /api/v1.0/Tuition4Year
# Query for the tuition cost for 4-year institutions by state for 2004-2018
# Returns the JSON representation of the dictionary.
@app.route("/api/v1.0/Tuition4Year")
def Tuition4Year_by_state():
    tuition4Year_results = list(mongo.db.tuition_4year_by_state.find({}, {'_id': False}))
    return jsonify(tuition4Year_results)

if __name__ == "__main__":
    app.run(debug=True)