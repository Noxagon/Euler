# Find the sum of the even-valued terms in the Fibonacci sequence whose values do not exceed four million

# List of first 2 Fibonacci number
fib = [1, 2]
i = 1
total = 0

while 1:
    # Add the subsequent Fibonacci number into the fib list
    fib.append(fib[i] + fib[i - 1])
    i += 1
    if fib[i] > 4000000:
        # If number exceeds 4 million, removes the number and stops the loop
        fib.remove(fib[i])
        break

for num in fib:
    if num % 2 == 0:
        # Total up the even Fibonacci numbers from the fib list
        total += num

print("List: " + str(fib))
print("Sum: " + str(total))
