# Find the largest palindrome made from the product of two 3-digit numbers
minNum = 10000   # Minimum product of two 3-digit numbers
maxNum = 998001  # Maximum product of two 3-digit numbers
maxPal = 0
i = 999   # Maximum 3-digit numbers

while minNum < maxNum:
    # Check if number is a palindrome
    if str(minNum) == str(minNum)[::-1]:
        # If number is a palindrome, check if it is a product of two 3-digit numbers
        for i in range(100, 999):
            if minNum % i == 0:
                if minNum // i in range(100, 999):
                    maxPal = minNum
                    break
    minNum += 1

print(str(maxPal) + " = " + str(i) + " x " + str(maxPal//i))
