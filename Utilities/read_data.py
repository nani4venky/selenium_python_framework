import csv


def getCSVData(fileName):
    # create a list to store rows
    rows = []
    # open CSV file
    data = open(fileName, "r")
    # create a CSV Reader from CSV File
    reader = csv.reader(data)
    # skip the headers
    next(reader)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows

