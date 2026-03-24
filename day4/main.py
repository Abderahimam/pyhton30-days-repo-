letter = "p"
print(letter)

sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)


multi_string = """I am student and i love learning new stuff that's why i decided to do this 30 days of pyton"""
print(multi_string)

language = "python"

print(language[0])

print(language[-3:])
print(language[1:6:2])


challenge = "i love this 30 days of python"

print(challenge.capitalize())

challenge = "i love this 30 days of python"

print(challenge.count("y"))

print(challenge.endswith("on")) #true
print(challenge.endswith("tion"))  #false 

print(challenge.find("y"))

first_name = "abderahim"
Last_name= "amari"
country = "Poland"

result = "i am {} {}. I live in {}. ".format(
    first_name, Last_name, country
)
print(result)  #i am abderahim amari. I live in Poland.

radius = 10
pi =3.14
area = pi * radius ** 2 
resultt = "the area of  circle with {} is {}. ".format(str(radius), str(area))
print(resultt)  #the area of  circle with 10 is 314.0.



# islower():Checks if all alphabets in a string are lowercase
challenge = "i love this 30 days of python"
print(challenge.islower())
challenge = "Thirty days of python"
print(challenge.islower())



challenge = "thirtyhy days of python"
print(challenge.isupper())

challenge = "THIRTY DAYS OF PYTHON"
print(challenge.isupper())  # True


challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))
print(challenge.split())

print(challenge.title())

print(challenge.swapcase())

