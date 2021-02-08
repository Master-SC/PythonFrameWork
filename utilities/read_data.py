import csv


def getCSVData(fileName):
    rows = []
    dataFile = open(fileName, "r")
    reader = csv.reader(dataFile)
    '''
    Skipping the First Row next(reader)
    '''
    next(reader)
    for row in reader:
        rows.append(row)
    return rows
