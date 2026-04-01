
try:
    print(10+"5")
except:
    print("something went wrong")



try:
    name = input("please enter your name: ")
    year_born = input("please enter the year you were born: ")
    age = 2027 - int(year_born)
    print(f"you are {name} and your age is {age}.")
except:
    print("something went wrong")




try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')

else:
    print('I usually run with the try block')
finally:
    print('I always run,')



try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)


def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e
lst = [ 1,2 , 3, 4, 5]
print(sum_of_five_nums(*lst))


countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin,sw,nor,rest)


numbers= [ 1,2 ,3 ,4, 5]
one, *middle, last = numbers
print(one,middle, last)


def unpacking_person_info(name, country, city, age):
    return f"{name} lives in {country}. he is {age} year old. "
dct = { "name": "Abderahim", "country": "Poland", "city": "Warsaw", "age": 20 }
print(unpacking_person_info(**dct))




def sum_all(*args):
    s = 0
    for i in args:
        s+= i
    return s
print(sum_all(1,2,3,4,5))
print(sum_all(1,2,3,4,5,6,7,8,9,10))



def packing_person_info(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs
print(packing_person_info(name="Abderahim", country="Poland", city="Warsaw", age=20))


lst_one = [1, 2, 3]
lst_two = [4, 5, 6]
LST = [0, *lst_one, *lst_two]
print(LST)



country_lst_one = ["Finland", "Sweden", "Norway"]
country_lst_two = ["Denmark", "Iceland"]
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)



for index, item in  enumerate([20,30, 40]):
    print(index, item)

countries = ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]
for index, i in enumerate(countries):
    if i == "finland":
     print(f"the country {i} has been found at index {index}")



#exercises: Day 13

#names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.

countries = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries, es, eu = countries
print(nordic_countries)
print(es)
print(eu)