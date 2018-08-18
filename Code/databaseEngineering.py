# import necessary libraries
import os
import pandas as pd
import pymongo
import json

def import_enrollment_content(filepath, collection_name):
    mng_client = pymongo.MongoClient('localhost', 27017)
    mng_db = mng_client['project2'] # Mongo db name
    db_cm = mng_db[collection_name]
    cdir = os.path.dirname('../Resources/EnrollmentByState/')
    file_res = os.path.join(cdir, filepath)

    data = pd.read_csv(file_res)
    data_json = json.loads(data.to_json(orient='records'))
    db_cm.remove()
    db_cm.insert(data_json)

def import_degree_content(filepath, collection_name):
    mng_client = pymongo.MongoClient('localhost', 27017)
    mng_db = mng_client['project2'] # Mongo db name
    db_cm = mng_db[collection_name]
    cdir = os.path.dirname('../Resources/DegreesByField/')
    file_res = os.path.join(cdir, filepath)

    data = pd.read_csv(file_res)
    data_json = json.loads(data.to_json(orient='records'))
    db_cm.remove()
    db_cm.insert(data_json)

def import_tuition_content(filepath, collection_name):
    mng_client = pymongo.MongoClient('localhost', 27017)
    mng_db = mng_client['project2'] # Mongo db name
    db_cm = mng_db[collection_name]
    cdir = os.path.dirname('../Resources/Tuition/')
    file_res = os.path.join(cdir, filepath)

    data = pd.read_csv(file_res)
    data_json = json.loads(data.to_json(orient='records'))
    db_cm.remove()
    db_cm.insert(data_json)

if __name__ == "__main__":
    # csv files to import
    HS_graduates_pct_chg_by_state = 'PublicHSGraduatesByState_percent.csv'
    enroll_4year_pct_chg_by_state = '4YearEnrollmentByState_percent.csv'
    tuition_4year_pct_chg_by_state = '4YearTuitionByState_percent.csv'
    bachelors_degrees_by_year = 'BachelorsDegreesAwardedByFieldofStudy_Clean.csv'

    # import csv files
    import_enrollment_content(HS_graduates_pct_chg_by_state, 'HS_graduates_pct_chg_by_state')
    import_enrollment_content(enroll_4year_pct_chg_by_state, 'enroll_4year_pct_chg_by_state')
    import_tuition_content(tuition_4year_pct_chg_by_state, 'tuition_4year_pct_chg_by_state')
    import_degree_content(bachelors_degrees_by_year, 'bachelors_degrees_by_year')
