#import DB Library
#connect to DB
#GET A CURSOR
#RUN SQL COMMANDS ON THE CURSOR
#COMMIT
#CLOSE CONNECTION

import urllib2, cookielib
import zipfile, os
import time
import sqlite3
from datetime import datetime
import os, csv

conn = sqlite3.connect('/data/pythondb.sqlite')

c = conn.cursor()

#c.execute('CREATE TABLE prices (SYMBOL text, SERIES text, OPEN real, HIGH real, LOW real, CLOSE real, LAST real, PREVCLOSE real, TOTTRDQTY real, TOTTRDVAL real, TIMESTAMP date, TOTALTRADES real, ISIN text, PRIMARY KEY (SYMBOL, SERIES, TIMESTAMP))')

conn.commit()

# def download(localZipFilePath,urlOfFileName):
#     hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
#            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#            'Accept-Encoding': 'none',
#            'Accept-Language': 'en-US,en;q=0.8',
#            'Connection': 'keep-alive'}
#     webRequest = urllib2.request.Request(urlOfFileName, headers=hdr)
#     try:
#         page = urllib2.request.urlopen(webRequest)
#         content = page.read()
#         output = open(localZipFilePath, "wb")
#         output.write(bytearray(content))
#         output.close()
#     except(urllib2.request.HTTPError, e):
#         print(e.fp.read())
#         print("Looks like the download did not go through. Please download manually \nFROM:" + urlOfFileName + "\nTO:" + localZipFilePath)
#
# def unzip(localZipFilePath, localExtractFilePath):
#     if os.path.exists(localZipFilePath):
#         print("Cool! " + localZipFilePath + " exists..proceeding")
#         listOfFiles = []
#         fh = open(localZipFilePath, 'rb')
#         zipFileHandler = zipfile.ZipFile(fh)
#         for name in zipFileHandler.namelist():
#             zipFileHandler.extract(name, localExtractFilePath)
#             listOfFiles.append(localExtractFilePath + name)
#             print("Extracted " + name + " from the zip file, and saved to " + (localExtractFilePath + name))
#         print("Extracted " + str(len(listOfFiles)) + " file in total")
#         fh.close()


# def downloadAndUnzipForPeriod(listOfMonths, listOfyears):
#     for year in listOfYears:
#         # indentation changes - we are inside the first for loop ( for the years)
#         for month in listOfMonths:
#             # indentation changes yet again - we are inside the second for loop ( for each  month in a given year)
#             for dayOfMonth in range(31) :
#                 # indentation changes yet again - this is being executed for each day of each month of each year
#                 # notice how we use the range(31) function to get a list with elements [0,1,2,....30]
#                 date = dayOfMonth + 1
#                 # lists are indexed from 0 but the dates start from 1, so add 1
#                 ############################################################################
#                 # OK the code that follows basically constructs a URL for the file
#                 # as saved in the NSE website. How do we know how to construct this?
#                 # Simply by manually downloading these files and examining the pattern for
#                 # different dates/months/years.
#                 # A typical URL looks like this : http://www.nseindia.com/content/historical/EQUITIES/2015/JUL/cm07JUL2015bhav.csv.zip
#                 #############################################################################
#                 # Convert number to string
#                 dateStr = str(date)
#                 # Note how single digit dates have a leading 0
#                 if date < 10:
#                     # indentation shows we are inside the if condition
#                     dateStr = "0"+dateStr
#                     # tack on a leading zero
#                 # indentation changes - we are out of the if loop
#                 print(dateStr, "-", month,"-", year)
#                 # Construct the filename
#                 fileName = "cm" +str(dateStr) + str(month) + str(year) + "bhav.csv.zip"
#                 # Construct the entire URL
#                 urlOfFileName = "http://www.nseindia.com/content/historical/EQUITIES/"+ year +"/"+ month + "/" + fileName
#                 # Construct the file on our local hard disk where we wish to save the downloaded file
#                 # The file path would look different on Windows machines - something like "C:/Users/vitthal/PythonCodeExamples/"
#                 localZipFilePath = "/Users/swethakolalapudi/PythonCodeExamples/" + fileName
#                 # Make the call to the download function
#                 download(localZipFilePath, urlOfFileName)
#                 # MAke the call to the unzip function
#                 unzip(localZipFilePath,localExtractFilePath)
#                 # We want to make sure that we don't inadvertently overwhelm the NSE website
#                 # so take a pause of 10 seconds to make sure we are not overloading it
#                 time.sleep(10)
#                 # done with all 3 for loops , the years, months and days
#     print("OK, all done downloading and extracting")
#
# #initialize a variable with a local directory in which to extract the
# # zip file above
# localExtractFilePath = "/Users/swethakolalapudi/PythonCodeExamples/"
#
#
#
# listOfMonths = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
# listOfYears = ['2014']
#
# downloadAndUnzipForPeriod(listOfMonths,listOfYears)

def insertRows(fileName, conn):
    c = conn.cursor()
    lineNum = 0
    with open(fileName, 'rb') as csvfile:
        lineReader = csv.reader(csvfile, delimiter=",", quotechar="\"")
    for row in lineReader
        lineNum = lineReader + 1
        if lineNum == 1:
            print "Skipping Header row"
