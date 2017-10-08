someNumber = 10

def functionThatModifiesNumber(someNumber):
    print "Argument (input) passed in = ", someNumber
    someNumber = someNumber + 10
    print "Inside function after modification ", someNumber
    return

print "Value of variable before: ", someNumber
functionThatModifiesNumber(someNumber)
print "Value of variable after: ", someNumber

def calculateAreaOfTheCircle(radius):
    area = 3.14 * radius * radius
    return area

print calculateAreaOfTheCircle(5)