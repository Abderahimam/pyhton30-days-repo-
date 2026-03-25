a = 3
if a > 0:
   print(" A is the positive number ")

b = 4

if b<0:
   print("B is a negative number ")

else:
   print("B is positive number")



c= 0
if c < 0:
   print("c is negative number")

elif c > 0:
   print("c is positive number")

else:
   print("c is zero")



d = 8
if d > 0:
   if d % 2 == 0:
      print('d is positive and integer')
   else:
      print(' IS a positive number')
elif d == 0:
   print('d is zero')

else:
   print('d is negative number')


   e = 0
   if e > 0 and e % 2 == 0:
      print("e is positive number and integer")
   elif e > 0 and e % 2 != 0:
      print("a is a positive")
   elif e == 0:
      print("e is zero")
   else:
      print(" e is negative")




user = "adm-tes"
access_level = 3
if user == "admin" or access_level >= 4:
   print("access granted")
else:
   print("access is denied")

   # exo 1 Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:



age = int(input("please enter you're age:"))
if age >=18:
   print(" you are old enough to drive")
else:
   years_left = 18 - age
   print(f" you need to wait {years_left} more years")



   # exo 2 Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:


my_age = 20
your_age = int(input("Please enter your age: "))

if my_age > your_age:
    age_diff = my_age - your_age
    if age_diff > 1:
        print(f"I am {age_diff} years older than you.")
    else:
        print(f"I am {age_diff} year older than you.")
elif your_age > my_age:
    age_diff = your_age - my_age
    if age_diff > 1:
        print(f"You are {age_diff} years older than me.")
    else:
        print(f"You are {age_diff} year older than me.")
else:
    print("We are the same age!")
