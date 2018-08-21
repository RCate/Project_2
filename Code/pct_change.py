import os
import csv

# Files to import
fourYear_csvpath = os.path.join('Resources', 'EnrollmentByState', '4YearEnrollmentByState_Clean.csv')
hs_csvpath = os.path.join('Resources', 'EnrollmentByState', 'PublicHSGraduatesByState_Clean.csv')
tuition_csvpath = os.path.join('Resources', 'Tuition', '4YearTuitionByState.csv')


# Output files
fourYear_output_file = os.path.join('Resources', 'EnrollmentByState', '4YearEnrollmentByState_percent.csv')
hs_output_file = os.path.join('Resources', 'EnrollmentByState', 'PublicHSGraduatesByState_percent.csv')
tuition_output_file = os.path.join('Resources', 'Tuition', '4YearTuitionByState_percent.csv')


def getPercentChange(infile, outfile):
    years = ['State', 'Y2009', 'Y2010', 'Y2011', 'Y2012', 'Y2013', 'Y2014', 'Y2015']
    state = []
    Y2009 = []
    Y2010 = []
    Y2011 = []
    Y2012 = []
    Y2013 = []
    Y2014 = []
    Y2015 = []

    with open(infile, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)

        #  Each row is read as a row
        for row in csvreader:
            state.append(row[0])
            Y2009.append((int(row[2])-int(row[1]))/int(row[1]))
            Y2010.append((int(row[3])-int(row[2]))/int(row[2]))
            Y2011.append((int(row[4])-int(row[3]))/int(row[3]))
            Y2012.append((int(row[5])-int(row[4]))/int(row[4]))
            Y2013.append((int(row[6])-int(row[5]))/int(row[5]))
            Y2014.append((int(row[7])-int(row[6]))/int(row[6]))
            Y2015.append((int(row[8])-int(row[7]))/int(row[7]))
            
        
    pct_chng = zip(state, Y2009, Y2010, Y2011, Y2012, Y2013, Y2014, Y2015)


    with open(outfile, "w", newline="") as datafile:
        writer = csv.writer(datafile)

        # Write the header row
        writer.writerow(years)

        # Write in zipped rows
        writer.writerows(pct_chng)

getPercentChange(fourYear_csvpath, fourYear_output_file)
getPercentChange(hs_csvpath, hs_output_file)
getPercentChange(tuition_csvpath, tuition_output_file)