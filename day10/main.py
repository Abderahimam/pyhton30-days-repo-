language = "python"
lst = list(language)
print(type(lst))
print(lst)

# Second way: list comprehension


lst = [i for i in language]
print(type(lst))
print(lst)


numbers = [i for i in range (11)]
print(numbers)
squares = [i * i for i in range (11)]
print(squares)

numbers = [(i, i* i) for i in range (11)]
print(numbers)


even_numbers = [i for i in range (21) if i % 2 == 0]
print(even_numbers)



odd_numbers = [i for i in range (21) if i % 2 == 1 ]
print(odd_numbers)


number = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_number =[ i for i in number if i % 2 == 0 and i > 0]
print(positive_even_number)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)

def add_two_nums (a,b):
    return a + b
print(add_two_nums(3, 5))

two_nums = lambda a, b: a + b 
print(two_nums(3, 5))


print( (lambda a, b : a+ b ) (4,5) )


square =lambda x : x ** 2
print(square(10))

cube = lambda x : x ** 3 
print(cube(3))


multiple_variable = lambda a, b , c : a**2 - 3*b +  4 * c
print(multiple_variable(2, 2,4))


def power(x):
    return lambda n: x**n
cube = power(2) (3)
print(cube)

#Exercises: Day 13
#Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
num=[i for i in numbers if i <= 0]
print(num)

#Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list =[row for number in list_of_lists for row in number]
print(flattened_list)
#vUsing list comprehension create the following list of tuples:
cool =[(n, 1, n**1, n**2, n**3, n**4, n**5) for n in range(11)]
for row in cool:
    print(row)


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_list = [row for country  in countries for row in country]
print(flattened_list)