# user input 
num = int(input("Enter your number: "))

factorial = 1

# if num is negative
if num < 0:
    print("Factorial does not exist for negative numbers.")
# if num is 0
elif num == 0:
    print("Factorial of 0 is 1")
# If +ve num greater the 0 
else:
    # for loop
    for i in range(1, num + 1):
        factorial = factorial * i

    print("Factorial of given number is:", factorial)
