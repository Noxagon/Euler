# Find the 10001st prime number
import math

prime = list()
primeNum = 3

prime.append(2)

# Make a list of 10001 prime numbers
while len(prime) < 10001:
    i = 0
    check = True

    while math.pow(prime[i], 2) <= primeNum:
        if primeNum % prime[i] == 0:
            check = False
        i += 1

    if check:
        prime.append(primeNum)

    primeNum += 2

print("10001st prime number: " + str(prime[10000]))
