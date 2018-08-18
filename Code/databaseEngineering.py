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
    HS_graduates_by_state = 'PublicHSGraduatesByState_Clean.csv'
    pct_chg_enroll_4year_by_state = '4YearEnrollmentByState_percent.csv'
    pct_chg_enroll_2year_by_state = '2YearEnrollmentByState_percent.csv'
    bachelors_degrees_by_year = 'BachelorsDegreesAwardedByFieldofStudy_Clean.csv'
    non_bachelors_degrees_by_year = 'NonBachelorsDegreesAwardedByFieldofStudy_Clean.csv'
    tuition_4year_by_state = '4YearTuitionByState.csv'
    tuition_2year_by_state = '2YearTuitionByState.csv'

    # import csv files
    import_enrollment_content(HS_graduates_by_state, 'HS_graduates_by_state')
    import_enrollment_content(pct_chg_enroll_4year_by_state, 'pct_chg_enroll_4year_by_state')
    import_enrollment_content(pct_chg_enroll_2year_by_state, 'pct_chg_enroll_2year_by_state')
    import_degree_content(bachelors_degrees_by_year, 'bachelors_degrees_by_year')
    import_degree_content(non_bachelors_degrees_by_year, 'non_bachelors_degrees_by_year')
    import_tuition_content(tuition_4year_by_state, 'tuition_4year_by_state')
    import_tuition_content(tuition_2year_by_state, 'tuition_2year_by_state')
