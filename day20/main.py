import pandas as pd
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s= pd.Series(nums)
print(s)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s= pd.Series(nums, index=[1, 2, 3, 4, 5, 6, 7, 8, 9])
print(s)

fruits = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
s= pd.Series(fruits, index=[1, 2, 3, 4, 5])
print(s)
dct = {"name": "Amine", "age": 30, "city": "New York"}
s = pd.Series(dct)
print(s)

s= pd,Series(10, index = [1, 2, 3, 4, 5])
print(s)


data = [
    ['Asabeneh', 'Finland', 'Helsink'],
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]

df = pd.DataFrame(data, columns=["Name", "Country", "City"])
print(df)

