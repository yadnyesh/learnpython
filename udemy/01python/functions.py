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

def calculateAreaAndCircumference(radiusList):
    areaResultList = []
    circumferenceResultList = []
    resultHash = {'Areas': areaResultList, 'Circumferences' : circumferenceResultList}

    for oneRadius in radiusList:
        areaResultList.append(3.14 * oneRadius * oneRadius)
        circumferenceResultList.append(3.14 * 2 * oneRadius)

    return resultHash

radiusList = [1,2,3,4]
resultMap = calculateAreaAndCircumference(radiusList)
print "For circles with radii = ", radiusList, "\nAreas = ", resultMap['Areas'], "\n Circumferences = ", resultMap['Circumferences']


