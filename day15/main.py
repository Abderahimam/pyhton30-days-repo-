import json 
person_json = '''{
    "name": "John",
    "age": 30,
    "city": "New York"
}'''

person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])


import csv
with open("./files/csv_example.csv") as f:
    csv_reader = csv.reader(f,delimiter=",")
    LINE_COUNT = 0
    for row in csv_reader:
        if LINE_COUNT == 0:
            print(f"columen names are :{', '.join(row)}")
            LINE_COUNT += 1
        else:
            print(
                f'\t{row[0]} is a teacher. he lives in{row[1]}, {row[2]}.')
            LINE_COUNT += 1
    print(f"Number of lines:{LINE_COUNT}")

import json 
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
person_json = json.dumps(person, indent=4)
print(type(person_json))
print(person_json)

import json 
person = {
    "name": "abderahim",
    "lastname": " amari",
    "country": "algeria",
    "skills": ["JavaScrip", "React", "Python"]
}
with open("./files/json_example.json", "w", encoding="utf-8") as f:
    json.dump(person, f, ensure_ascii=False, indent=4)

 import xlrd
excel_book = xlrd.open_workbook("sample.xlx")
print(excel_book.nsheets)
print(excel_book.sheet_names)
            






f = open("./files/hello_world.txt")
txt = f.read()
print(type(txt))
print(txt)
f.close()

f = open("./files/hello_world.txt")
txt = f.read(10)
print(type(txt))
print(txt)
f.close()

f = open("./files/hello_world.txt")
txt= f.readline()
print(type(txt))
print(txt)
f.close()


f = open("./files/hello_world.txt")
txt= f.readlines()
print(type(txt))
print(txt)
f.close()


f = open("./files/hello_world.txt")
lines= f.read().splitlines()
print(type(lines))
print(lines)
f.close()



with open("./files/hello_world.txt") as f:
    txt = f.read().splitlines()
    print(type(txt))
    print(txt)
 
 
with open ("./files/hello_ishak.txt", "a") as f:
    f.write("this text has to be appended at the end")


with open ("./files/hello_ishak.txt", "w") as f:
    f.write("this text will be written in a newly created file")



import os
if os.path.exists("./files/hello_ishak.txt"):
    os.remove("./files/hello_ishak.txt")
else:
    print("the file does not exist")
            