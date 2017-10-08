import csv

oneFileName = "/home/yadnyesh/tuts/learnpython/udemy/01python/files/cm17JUL2017bhav.csv"

lineNum = 0;

#with - Opens the file
with open(oneFileName, "rb") as csvFile:
    listOfLists = []
    lineReader = csv.reader(csvFile, delimiter=",",quotechar="\"")
    for row in lineReader:
        lineNum = lineNum + 1
        if lineNum == 1:
            print "Skipping the header row"
            continue
        symbol = row[0]
        close = row [5]
        prevClose = row[7]
        tradedQty = row[9]
        pctChange = float(close) / float(prevClose) - 1
        oneResultRow = [symbol, pctChange, float(tradedQty), float(pctChange)]
        listOfLists.append(oneResultRow)
        print symbol, "{:,.1f}".format(float(tradedQty)/1e6) + "M INR", "{:,.1f}".format(pctChange*100)+"%"
              #symbol, "{:,.1f}".format(float(tradedQty)/1e6) + "M INR", "{:,.1f}".format(pctChange*100)+"%"
    print "Done Iterating over file....the file will be closed now!"
    print "We have information for " + str(len(listOfLists)) + " stocks"
    print listOfLists

#listOfListsSortedByQty = sorted(listOfLists, key=lambda x:x[2], reverse=True)
listOfListsSortedByQty = sorted(listOfLists, key=lambda x:x[1], reverse=True)

print listOfListsSortedByQty


import xlsxwriter

excelFileName = "/home/yadnyesh/tuts/learnpython/udemy/01python/files/cm17JUL2017bhav.xlsx"

workbook = xlsxwriter.Workbook(excelFileName)
worksheet = workbook.add_worksheet("Summary")

worksheet.write_row("A1", ["Top Traded Stocks"])
worksheet.write_row("A2", ["Stock", "%Change", "Value Traded (INR"])

for rowNum in range(5):
    oneRowtoWrite = listOfListsSortedByQty[rowNum]
    worksheet.write_row("A" + str(rowNum + 3), oneRowtoWrite)
workbook.close()