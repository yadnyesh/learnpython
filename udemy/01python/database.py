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

conn = sqlite3.connect('/data/pythondb.sqlite')

c = conn.cursor()

c.execute('CREATE TABLE prices (SYMBOL text, SERIES text, OPEN real, HIGH real, LOW real, CLOSE real, LAST real, PREVCLOSE real, TOTTRDQTY real, TOTTRDVAL real, TIMESTAMP date, TOTALTRADES real, ISIN text, PRIMARY KEY (SYMBOL, SERIES, TIMESTAMP))')

conn.commit()

def download(localZipFilePath,urlOfFileName):
    # We already wrote the code for this bit in the drill on files. Lets just copy that over
    # This bit of boiler plate code below is needed because the
    # website of the National Stock Exchange tries to block automated
    # programs (like this one!) from downloading files.
    # This line is not needed with all websites, but there are a reasonable
    # number that will block automated downloads, in which case the additional line below
    # will circumvent the block.
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}

    # here below is the code that actually downloads the page and stores to file

    # Make the web request - just as a web browser like Chrome or Mozilla would
    # Note that we pass in the boilerplate code we just typed above
    webRequest = urllib2.request.Request(urlOfFileName, headers=hdr)

    # Doing stuff with files is quite prone to errors in the disk or in the network
    # connection, so use a try:/except: pair as safety net
    try:
        # Make the web request
        page = urllib2.request.urlopen(webRequest)
        # Save the contents of the web request in a variable called 'content'.
        # These contents are literally the zip file from the URL (i.e. what you'd get
        # if you downloaded the URL manually)
        content = page.read()
        # Save the contents to the zip file on disk locally
        # 1. open the barrel (file). The 'w' signifies that we intend to write, i.e
        # put stuff into the barrel (file)
        output = open(localZipFilePath, "wb")
        # 2. write contents to file, i.e. actually put stuff in the barrel
        output.write(bytearray(content))
        # 3. close the barrel (i.e. the file)
        output.close()
    # this bit below, the except: block is what will get executed if any of the lines above throw errors
    except(urllib2.request.HTTPError, e):
        # print out exactly what error, if any, resulted
        print(e.fp.read())
        # Let the user know that the download did not work, and that file needs to be manually downloaded
        print("Looks like the download did not go through. Please download manually \nFROM:" + urlOfFileName + "\nTO:" + localZipFilePath)

