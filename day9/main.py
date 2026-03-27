import mymodule
print(mymodule.generate_full_name("abderahim" , "amari"))







from statistics import * 
ages = [ 20, 20, 4, 24, 25, 26, 22, 20, 23, 22, 26]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))


import math

print(math.pi)
print(math.sqrt(2))
print(math.pow(2, 3))
print(math.log10(100))

from math import * 

from math import pi as PI
print(PI)


import string
print(string.ascii_letters)


from random import random, randint
print(random())



# Task 1 — Generate a random 6‑character user ID

import string
import random

def random_user_id():
    charachter = string.ascii_letters + string.digits 
    user_id = "".join(random.choice(charachter) for _ in range(6))
    return user_id
print(random_user_id())


# Task 2 — Generate multiple user IDs with custom length
import string
import random

def user_id_gen_by_user():
    length = int(input("enter id length: "))
    count = int(input("Enter how many ID's you want : "))

    charachter = string.ascii_letters + string.digits
    for _ in range (count):
        user_id = "". join(random.choice(charachter) for _ in range (length))
        print(user_id)
    
user_id_gen_by_user()





import random

def rgb_color_gen():
    r = random.randint(0, 255)  # red value
    g = random.randint(0, 255)  # green value
    b = random.randint(0, 255)  # blue value
    return (r, g, b)

print(rgb_color_gen())
