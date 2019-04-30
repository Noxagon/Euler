# Find the largest prime factor of the number 600851475143

# Smallest prime number is 2
i = 2
num = 600851475143

while 1:
    if num % i == 0:
        # If the remainder is 0, the number will be divided by 'i'
        # 'i -= 1' will run to check if the number is divisible by 'i' again
        num /= i
        i -= 1
        if num == 1:
            print("Answer: " + str(i+1))
            break
    i += 1
