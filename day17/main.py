class Person:
 pass

print(Person)


p = Person()
print(p)   




class Person:
    def __init__ (self, name):
        self.name = name

p = Person("abderahim")
print(p.name)
print(p)




class Person:
    def __init__ (self, firstname, lastname, age, country, city):
       self.firstname = firstname
       self.lastname = lastname 
       self.age = age
       self.country = country
       self.city = city
       
p = Person("abderahim", " amari", 20, "Poland", "Krakow")
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)


#Object Methods



class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):

        return f'{self.firstname} {self.lastname} is {self.age} years old and lives in {self.city}, {self.country}.'
p = Person("abderahim", "Amari", 20, "Poland", "Krakow")
print(p.person_info())


class Person:
    def __init__(self, firstname= "abderahim", lastname= " Amari", age= 20, country= "poland", city= "krakow"):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
    def person_info(self):
        return f"{self.firstname} {self.lastname}, is{self.age} years old. he lives in {self.city}, {self.country}."
p1 = Person()
print(p1.person_info())
p2 = Person("jhon", "moe", 30, "Poland", "warsaw") 
print(p2.person_info())




class Person:
    def __init__(self, firstname= "abderahim", lastname= " Amari", age= 20, country= "poland", city= "krakow"):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []
    def person_info(self):
        return f"{self.firstname} {self.lastname}, is{self.age} years old. he lives in {self.city}, {self.country}."
    def add_skill(self, skill):
        self.skills.append(skill)


p1 = Person()
print(p1.person_info())
p1.add_skill("Python")
print(p1.skills)
p1.add_skill("JavaScript")
p2 = Person("jhon", "cezar", 38, "norway", "oslo")
print(p2.person_info())
p2.add_skill("JavaScript")
print(p2.skills)


class Student(Person):
    pass
s1 = Student("ayoub", "amine", 22, "algeria", "algiers")
s2 = Student("younes", "amine", 22, "algeria", "algiers")
print(s1.person_info())
s1.add_skill("javascript")
s1.add_skill("react")
print(s1.skills)
print(s2.person_info())
s2.add_skill("python")  
print(s2.skills)
