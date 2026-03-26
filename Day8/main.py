def generate_full_name ():
    first_name = "abderahim"
    last_name = "amari"
    space = " "
    full_name = first_name + space + last_name 
    print(full_name)

generate_full_name()

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
    
add_two_numbers()


def generate_full_name ():
    first_name = "Abderahim"
    last_name = "Amari"
    space = " "


    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())


def add_numbers():
    num_one = 4
    num_two = 4
    total = num_one + num_two
    return total
print(add_numbers())




def greetings (name):
    message = name + ",welcom to python for everyone !"
    return message
print(greetings("rahimo"))

def add_ten(num):
    ten = 10
    return num +ten
print(add_ten(50))

def square_number (x):
    return x * x
print(square_number(5))
    

def area_of_circle (r):
    pi = 3.14
    area = pi * r ** 2 
    return area
print(area_of_circle(10))



def sum_of_numbers(n):
    total = 0
    for i in range (n+1):
        total+=i
    return total
print(sum_of_numbers(10)) #55
print(sum_of_numbers(100))  #5050


def generate_full_name (first_name , last_name):
    space = " "
    full_name = first_name + space + last_name
    return full_name
print("Full name:",generate_full_name("abdel", "amari"))

def su_num (nu_uno , nu_two):
    total = nu_uno + nu_two
    return total
print("sum of the two number are:", su_num(15, 30))



def calculate_age (current_year , birth_year):
    age = current_year - birth_year
    return age
print(" you are :", calculate_age (2026 , 2005), "years old")



def weight_of_object (mass, gravity):
    weight = str(mass*gravity) +" N"
    return weight
print("weight:", weight_of_object (90,9.81))



def is_even (n):
    if n % 2 == 0:
        return True
    return False 
print(is_even(10))

print(is_even(11))

  
def find_evem_num (n):
    evens = []
    for i in range (n+1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_evem_num(15))



#dafault param

def greetings(name = " jaksom"):
    message = name + ", wlcom to python class"
    return message 
print(greetings())
print(greetings("rahim"))


def sum_of_nums (*nums):
    total = 0 
    for num in nums:
        total+=num
    return total
print(sum_of_nums(5, 6, 8, 10))  #29



def greet(name , location):
    print("Hi there", name, "how's the weather in", location)

greet(name = "rahim" , location = "poland")
#Hi there rahim how's the weather in poland

my_dict = {"name":"ishak", "location":"oran"}
greet(**my_dict)



def area_of_cer(r):
    PI = 3.14

    area = PI * r * r
    return area
print(area_of_cer(10))

#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def convert_celsius_to_fahrenheit(C):
   F = ( C*(9%5)) + 32 
   return F
print(convert_celsius_to_fahrenheit(23))