import urllib2

urlOfFileName = "http://www.nseindia.com/content/historical/EQUITIES/2017/OCT/cm06OCT2017bhav.csv.zip"
localZipFilePath = "/home/yadnyesh/tuts/learnpython/udemy/01python/files"
hdr = {
        'items' : { 'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Encoding:gzip, deflate, sdch, br',
                    'Accept-Language:en-GB,en-US;q=0.8,en;q=0.6',
                    'Cache-Control:no-cache',
                    'Connection:keep-alive',
                    'Cookie:NSE-TEST-1=1826627594.20480.0000',
                    'Host:www.nseindia.com',
                    'Pragma:no-cache',
                    'Referer:https://www.nseindia.com/products/content/all_daily_reports.htm',
                    'Upgrade-Insecure-Requests:1',
                    'User-Agent:Mozilla/5.0 (X11; ,Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                 }
}
webRequest = urllib2.Request(urlOfFileName, headers= hdr)

try:
    page = urllib2.urlopen(webRequest)
    content = page.read()
    output = open(localZipFilePath, "wb")
    output.write(bytearray(content))
    output.close()
except urllib2.HTTPError, e:
    print e.fp.read()
    print "Looks like a malformed URL"
