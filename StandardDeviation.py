#Write a function that generates random marks for the 100 students
#Write a function that calculates the mean

import random
import matplotlib.pyplot as plt
import math

marks = []
x = []

#def generateRandomMark():
#   for x in range(100):
#        marks.append(random.randint(1,100))
#        return marks


def generateRandom2():
    marks = [random.randrange(0,100) for i in range(100)]
    return marks

def generateMean(listL):
     # print sum(listL) / len(listL)
     total = 0
     for i in range(len(listL)):
         total += listL[i]
         mean = total/len(listL)
     return mean

def generateVariance(listL, mean):
    temp = []
    for i in listL:
        temp.append(listL[i] - mean)
        
    return temp

def generateStandardDev(listL, mean):
    tempVariance = []
    sqVariance =  0
    tempSquareVariance = 0
    stdDev = []
    for i in listL:
        variance = listL[i] - mean
        sqVariance = variance * variance
        tempSquareVariance += sqVariance
        #stdDev.append(math.sqrt(tempSquareVariance/(len(listL)-1)))
        stdDev = math.sqrt(tempSquareVariance/(len(listL)-1))
    return stdDev

listOfMarks = []
listOfMarks = generateRandom2()
mean = generateMean(listOfMarks)

print ("The list of random marks is: \n")
print (generateRandom2())

print ("\n\nThe mean of marks is: \n")
print (generateMean(generateRandom2()))

print ("\n\nThe variance for the whole list of marks is: \n")
print (generateVariance(listOfMarks, mean))

print ("\n\nThe standard deviation is: \n")
print (generateStandardDev(listOfMarks, mean))

x = []
x.extend(range(0,100))
y = generateVariance(listOfMarks, mean)

plt.scatter(x, y)
plt.show()

plt.plot(x,y)
