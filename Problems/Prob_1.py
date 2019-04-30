# Find the sum of all the multiples of 3 or 5 below 1000
i = 0

for x in range(1000):
    # Checking the multiples of 3 or 5
    if x % 5 == 0 or x % 3 == 0:
        i += x

print('Total: ' + str(i))
