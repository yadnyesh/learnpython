import zipfile, os

localZipFilePath = "/home/yadnyesh/tuts/learnpython/udemy/01python/files/cm17JUL2017bhav.csv.zip"
localExtractFilePath = "/home/yadnyesh/tuts/learnpython/udemy/01python/files"

if os.path.exists(localZipFilePath):
    print localZipFilePath + " exists!"
    listOfFiles = []
    fh = open(localZipFilePath, 'rb') #read mode for file
    zipFileHandler = zipfile.ZipFile(fh)

    for filename in zipFileHandler.namelist():
        zipFileHandler.extract(filename, localExtractFilePath)
        listOfFiles.append(localExtractFilePath + filename)
        print "Extracted " + filename + "from zip file to " + (localExtractFilePath + "/" + filename)
    print "Total, we extracted ", str(len(listOfFiles)), " files "
    fh.close()
