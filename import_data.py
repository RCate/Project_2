import os
import csv

# Files to import
fourYear_csvpath = os.path.join('Resources', 'EnrollmentByState', '4YearEnrollmentByState_Clean.csv')
twoYear_csvpath = os.path.join('Resources', 'EnrollmentByState', '2YearEnrollmentByState_Combined.csv')


# Output files
fourYear_output_file = os.path.join('Resources', 'EnrollmentByState', '4YearEnrollmentByState_percent.csv')
twoYear_output_file = os.path.join('Resources', 'EnrollmentByState', '2YearEnrollmentByState_percent.csv')


def getPercentChange(infile, outfile):
    years = ['State', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    state = []
    Y2002 = []
    Y2003 = []
    Y2004 = []
    Y2005 = []
    Y2006 = []
    Y2007 = []
    Y2008 = []
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
            Y2002.append((int(row[2])-int(row[1]))/int(row[1]))
            Y2003.append((int(row[3])-int(row[2]))/int(row[2]))
            Y2004.append((int(row[4])-int(row[3]))/int(row[3]))
            Y2005.append((int(row[5])-int(row[4]))/int(row[4]))
            Y2006.append((int(row[6])-int(row[5]))/int(row[5]))
            Y2007.append((int(row[7])-int(row[6]))/int(row[6]))
            Y2008.append((int(row[8])-int(row[7]))/int(row[7]))
            Y2009.append((int(row[9])-int(row[8]))/int(row[8]))
            Y2010.append((int(row[10])-int(row[9]))/int(row[9]))
            Y2011.append((int(row[11])-int(row[10]))/int(row[10]))
            Y2012.append((int(row[12])-int(row[11]))/int(row[11]))
            Y2013.append((int(row[13])-int(row[12]))/int(row[12]))
            Y2014.append((int(row[14])-int(row[13]))/int(row[13]))
            Y2015.append((int(row[15])-int(row[14]))/int(row[14]))
        
    pct_chng = zip(state, Y2002, Y2003, Y2004, Y2005, Y2006, Y2007, Y2008, Y2009, Y2010, Y2011, Y2012, Y2013, Y2014, Y2015)


    with open(outfile, "w", newline="") as datafile:
        writer = csv.writer(datafile)

        # Write the header row
        writer.writerow(years)

        # Write in zipped rows
        writer.writerows(pct_chng)

getPercentChange(fourYear_csvpath, fourYear_output_file)
getPercentChange(twoYear_csvpath, twoYear_output_file)