# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
import math

sqrSum = 0
sumAll = 0
sumSqr = 0
sumDiff = 0

# Find the sum of the squares of the first 100 numbers and the sum of first 100 numbers
for i in range(100):
    sqrSum += math.pow(i+1, 2)
    sumAll += (i + 1)

# Find the square of the sum
sumSqr = math.pow(sumAll, 2)
sumDiff = sumSqr - sqrSum

print(str(sumSqr) + " - " + str(sqrSum) + " = " + str(sumDiff))
