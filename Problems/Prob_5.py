# Find the smallest positive number that is evenly divisible by all of the numbers from 1 to 20
import math
primeList = []
factorList = []

num = 0
res = 1
numLen = 20
primeNum = 3
primeLog = 0
primeList.append(2)

# Make a list of prime numbers between 1 and 20
while primeNum < numLen:
    i = 0
    check = True

    while math.pow(primeList[i], 2) <= primeNum:
        if primeNum % primeList[i] == 0:
            check = False
        i += 1

    if check:
        primeList.append(primeNum)

    primeNum += 2

# Find all of the LCMs for 1 to 20
while num < len(primeList):
    primeLog = math.floor(math.log(numLen, primeList[num]))
    factorList.append(math.pow(primeList[num], primeLog))
    num += 1

# Multiply all of the LCMs
for m in factorList:
    res *= m

print("Result: " + str(res))
