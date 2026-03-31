def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3




def absolute(x):
    if x> 0:
        return x
    else:
        return -(x)
print(absolute(-5))

def higher_order_function(type):
    if type == "square":
        return square
    elif type == "cube":
        return cube
    elif type == "absolute":
        return absolute

result = higher_order_function("cube")
print(result(3))
result = higher_order_function("square")
print(result(3))
result = higher_order_function("absolute")  
print(result(-3))




def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add
closure_result= add_ten()
print(closure_result(5))
print(closure_result(10))



def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("i live in {}".format(para3))
    return wrapper_accepting_parameters
    
@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("i am {} {} and i love to learn " .format(first_name, last_name,))
         
print_full_name("abderahim", "amari", "algeria")



numbers = [ 1,2,3,4,5]
def square (x):
     return x**2 
number_squared= map(square,numbers)
print(list(number_squared))



number_squared = map(lambda x: x**2, numbers)
print(list(number_squared))


names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
def change_to_upper(name):
    return name.upper()
names_upper_cased = map(change_to_upper,names)
print(list(names_upper_cased))



numbers = [ 1,2,3,4,5]
def is_even(num):
    if num % 2 == 0:
        return True
    return False
even_number = filter(is_even, numbers)
print(list(even_number))