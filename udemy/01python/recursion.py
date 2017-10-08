def reverseStringRecursive(someString):
    if someString is None:
        return someString

    if (len(someString)) <= 1:
        return someString

    return reverseStringRecursive(someString[1:]) + someString[0]

someString = "Yadnyesh"

print "The reverse of ", someString, " is", reverseStringRecursive(someString)