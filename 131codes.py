# 1.	Python program to add two numbers
# user input
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

# Adding...
result = num1 + num2

# print the added num
print("The sum of two numbers is : ", result)


# 2.	Maximum of two numbers in Python
# user input
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

# maximum of value
maximum_value = max(num1, num2)

# print the value
print("The maximum of two number:",maximum_value)

# 3.	Python Program for factorial of a number
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

# 4.	Python Program for simple interest
principal_amount=int(input("Enter the principal amount: "))
time=int(input("Enter the time period (in years): "))
rate=int(input("Enter the rate of interest (in percentage): "))


# calculate simple intrest
si=principal_amount*rate*time/100

print("Simple intrest is:" ,si)

# 5.	Python Program for compound interest
principal_amount=int(input("Enter the principal amount: "))
time=int(input("Enter the time period (in years): "))
rate=int(input("Enter the rate of interest (in percentage): "))

# calculate Compound intrest
amount=principal_amount*(pow((1+rate/100),time))
ci=amount-principal_amount

print("Compound intrest is:" ,ci)

# 6.	Python Program to check Armstrong Number

def is_armstrong_number(number):

    num_str = str(number)
    num_digits = len(num_str)

    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)

    return sum_of_digits == number

num = int(input("Enter a number: "))

if is_armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")


# 7.	Python Program for Program to find area of a circle
radius = float(input("Enter radius of circle: "))
area=3.14156*radius*radius
print("Area of circle is:",area)

# 8.	Python program to print all Prime numbers in an Interval

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def print_primes_in_interval(start, end):
    print(f"Prime numbers in the interval [{start}, {end}]:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")

start_num = int(input("Enter the start of the interval: "))
end_num = int(input("Enter the end of the interval: "))

print_primes_in_interval(start_num, end_num)

# 9.	Python program to check whether a number is Prime or not

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

# 10.	Python Program for n-th Fibonacci number

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = int(input("Enter the value of n: "))

result_recursive = fibonacci_recursive(n)
print(f"The {n}-th Fibonacci number (recursive) is: {result_recursive}")

# 11.	Python Program for How to check if a given number is Fibonacci number?

import math

def is_perfect_square(num):
    root = int(math.sqrt(num))
    return num == root * root

def is_fibonacci_number(number):
    if number < 0:
        return False

    return is_perfect_square(5 * number * number + 4) or is_perfect_square(5 * number * number - 4)

num = int(input("Enter a number: "))

if is_fibonacci_number(num):
    print(f"{num} is a Fibonacci number.")
else:
    print(f"{num} is not a Fibonacci number.")

# 12.	Python Program for n\’th multiple of a number in Fibonacci Series

def find_nth_multiple_in_fibonacci(number, n):
    if n <= 0:
        return "Invalid input: n should be a positive integer."

    fib_sequence = [0, 1]
    count = 2

    while count <= n:
        current_fibonacci = fib_sequence[-1] + fib_sequence[-2]

        if current_fibonacci % number == 0:
            count += 1

        fib_sequence.append(current_fibonacci)

    return f"The {n}-th multiple of {number} in the Fibonacci series is: {fib_sequence[-1]}"


num = int(input("Enter the number for which you want to find the multiple: "))
nth = int(input("Enter the value of n: "))

result = find_nth_multiple_in_fibonacci(num, nth)
print(result)

# 13.	Program to print ASCII Value of a character

character = input("Enter a character: ")

if len(character) == 1:
    # Printing the ASCII value of the character
    ascii_value = ord(character)
    print(f"The ASCII value of '{character}' is: {ascii_value}")
else:
    print("Please enter a single character.")

# 14.	Python Program for Sum of squares of first n natural numbers

def sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))

n = int(input("Enter the value of n: "))

result = sum_of_squares(n)
print(f"The sum of squares of the first {n} natural numbers is: {result}")

# 15.	Python Program for cube sum of first n natural numbers

def sum_of_cubes(n):
    return sum(i**3 for i in range(1, n+1))

n = int(input("Enter the value of n: "))

result = sum_of_cubes(n)
print(f"The sum of cubes of the first {n} natural numbers is: {result}")

# Array Programs:
# To scale up Array logic, try out the below-listed Python array programming examples. Here, you will find all the important Python examples that are related to the Python array concept.
# 1.	Python Program to find sum of array

def array_sum(arr):
    total_sum = 0
    for element in arr:
        total_sum += element
    return total_sum

arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

result = array_sum(arr)
print(f"The sum of the array is: {result}")

# 2.	Python Program to find largest element in an array

def find_largest_element(arr):
    if not arr:
        return "Array is empty, no largest element."

    largest_element = arr[0]
    for element in arr:
        if element > largest_element:
            largest_element = element

    return largest_element

arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

result = find_largest_element(arr)
print(f"The largest element in the array is: {result}")

# 3.	Python Program for array rotation

def rotate_left(arr, d):
    n = len(arr)
    d = d % n
    return arr[d:] + arr[:d]

def rotate_right(arr, d):
    n = len(arr)
    d = d % n
    return arr[-d:] + arr[:-d]

arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
rotation_count = int(input("Enter the number of positions to rotate: "))

rotated_left = rotate_left(arr, rotation_count)
rotated_right = rotate_right(arr, rotation_count)

print(f"Original array: {arr}")
print(f"Array after left rotation by {rotation_count} positions: {rotated_left}")
print(f"Array after right rotation by {rotation_count} positions: {rotated_right}")

# 4.	Python Program for Reversal algorithm for array rotation

def reverse_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array_reversal(arr, rotation_count):
    n = len(arr)
    rotation_count = rotation_count % n

    reverse_array(arr, 0, rotation_count - 1)

    reverse_array(arr, rotation_count, n - 1)

    reverse_array(arr, 0, n - 1)

arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
rotation_count = int(input("Enter the number of positions to rotate: "))

rotate_array_reversal(arr, rotation_count)
print(f"Array after rotation using reversal algorithm: {arr}")

# 5.	Python Program to Split the array and add the first part to the end

def split_and_add(arr, position):
    n = len(arr)
    position = position % n

    result = arr[position:] + arr[:position]

    return result

arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
split_position = int(input("Enter the position to split the array: "))

result = split_and_add(arr, split_position)
print(f"Array after splitting and adding the first part to the end: {result}")

# 6.	Python Program for Find reminder of array multiplication divided by n

def remainder_of_array_multiplication(arr, n):
    product = 1

    for num in arr:
        product = (product * num) % n

    return product % n

arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
n = int(input("Enter the value of n: "))

result = remainder_of_array_multiplication(arr, n)
print(f"The remainder of array multiplication divided by {n} is: {result}")

# 7.	Python Program to check if given array is Monotonic

def is_monotonic(arr):
    increasing = decreasing = True

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            increasing = False
            break

    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            decreasing = False
            break

    return increasing or decreasing

arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

if is_monotonic(arr):
    print("The array is monotonic.")
else:
    print("The array is not monotonic.")


