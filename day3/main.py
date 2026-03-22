# Arithmetic Operations in Python
# Integers

print("addition:", 1+2)
print("subtraction:", 2-1)
print("multiplication:", 2*3)


# Division in python gives floating number

print("division:", 4/2)
print("division:", 6/2)
print("division:", 8/2)
# gives without the floating number or without the remaining
print('Division without the remainder: ', 7 // 2)
print('Modulus: ', 3 % 2)                           # Gives the remainder
print('Division without the remainder: ', 7 // 3)
print("exponential:", 3**3)                       # it means 3 * 3 * 3


# Complex numbers
print("multiplying complex number:", (1+1j) * (1-1j))

# Declaring the variable at the top first

a = 3  # a is a variable name and 3 is an integer data type
b = 2  # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable


total = a + b 
dif = a - b
product = a * b 
division = a / b 
remainder = a % b 
floor_division = a // b 
exponential = a ** b 

print("a+b:", total)

print("a-b:", dif)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)



# Calculating area of a circle
radius = 10
area_of_circle = 3.14 * radius **2
print("area of circle:", area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print("area of rectengle:", area_of_rectangle)


print(3>2)
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2


print(3>2 and 4>2)
print(3 > 2 and 4 < 3)  # False - because the second statement is false
print(3 < 2 and 4 < 3)  # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false


print(not 3 > 2)
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False)  # False