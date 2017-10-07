import urllib2
import sys

print "Test"

urlToRead = "http://www.google.com"
crawledWebLinks = {}

while urlToRead != '':
    try:
        urlToRead = input("Please enter the URL to crawl: ")
        if urlToRead == "":
            print "OK, exiting loop"
            break
        shortName = input("Please enter a short name for that url: " + urlToRead + " ")
        webFile = urllib2.urlopen(urlToRead).read()
        crawledWebLinks[shortName] = webFile
    except:
        print "******\nUnexpected Error**************", sys.exc_info()[0]
        stopOrProceed = input("Enter 1 to stop, anything else to proceed..")
        if stopOrProceed ==1:
            print "Exiting the program"
            break
        else:
            print "Let's Continue\n"
            continue
    print "Inside while loop ...outside try catch"
print "Outside while loop "
print crawledWebLinks.keys()
print crawledWebLinks.values()