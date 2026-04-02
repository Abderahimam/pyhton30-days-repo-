import re


txt = "i love learn python in this 30 days of python"
match = re.match("i love learn python", txt, re.I)
print(match)

span = match.span()
print(span)

start, end = span
print(start,end)
substring = txt[start:end]
print(substring)



import re 
txt = "i love to learn python in this 30 days of python"
match = re.match("I like to learn", txt, re.I)
print(match)



import re 
txt = "python is the most beautiful language that a human being has ever created.i recommend python for a first programming language"
search = re.search("first", txt, re.I)
print(search)

span = search.span()
print(span)

start,end = span
print(start,end)
substring = txt[start:end]
print(substring)

import re 
txt = "python is the most beautiful language that a human being has ever created.i recommend python for a first programming language"
matches = re.findall("language", txt, re.I)
print(matches)



import re 
txt = "python is the most beautiful language that a human being has ever created.i recommend python for a first programming language"
matches = re.findall("python", txt, re.I)
print(matches)

import re 
txt = "python is the most beautiful language that a human being has ever created.i recommend python for a first programming language"
match_replaced= re.sub("python|Python", "javaScript", txt, re.I)
print(match_replaced)
match_replaced= re.sub("[Pp]ython", "javaScript", txt, re.I)
print(match_replaced)


import re 
txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

replace =re.sub("%", "", txt)
print(replace)

#I am teacher and  I love teaching.There is nothing as rewarding as educating and empowering people.I found teaching more interesting than any other jobs.Does this motivate you to be a teacher?               

import re 


txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt))



import re 
regex_patter = r"apple"
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_patter, txt,re.I)
print(matches)


import re 

regex= r"\d"
txt = "This regular expression example was made in January 12, 2020."
print(re.findall(regex, txt))
import re 
regex= r"\d+"
txt = "This regular expression example was made in January 12, 2020."
print(re.findall(regex, txt))

#Exercises: Level 3 Clean the following text. 

import re 

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
cleared_sentence = re.sub(r"[@$&#\%]+", "", sentence)
print(cleared_sentence  )

