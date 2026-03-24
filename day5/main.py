fruits = ["banana","orange", "mango", "lemon"]

vegatables = ["tomato", "onion", "potato", "carrot"]

countries = ["Poland","france","sweeden","USA"]


print("fruits:", fruits)
print("number of fruits:", len(fruits))
print("egatables:", vegatables)
print("number of vegatables is :", len(vegatables))

first_fruits = fruits[0]
print(first_fruits)

second_fruits = fruits[1]
print(second_fruits)

print(fruits[-1])

print(fruits[0:4])
print(fruits[0:])

fruits.insert(2,"apple")
print(fruits)

fruits.remove
print(fruits)


del fruits[0]
print(fruits)

del fruits[1]
print(fruits)



fruits_vegatables= fruits +vegatables 
print(fruits_vegatables)




fruits.clear()
print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)


ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

ages.sort(reverse=True)
print(ages)