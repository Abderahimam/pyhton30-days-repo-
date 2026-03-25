count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

count = 1 
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
         break
    



count = 0
while count < 6:
    if count == 2:
        count += 2
        continue
    print(count)
    count = count + 1





numbers = [ 1,2, 3, 4, 5, 6]
for number in numbers:
    print(number)
    if number == 3:
        break





language = "french"
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])



numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue 
    print("next number should be ", number + 1 ) if number != 5 else print("loop's end")

print("outside the loop")



for i in range (1, 10):
    print("**" * i)



for i in range (8):
    print("#"*8)



for i in range (0,10):
    print(f"{i} *{i} = {i*i}")

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
tech_list = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in tech_list:
    print(item)

# Use for loop to iterate from 0 to 100 and print only even numbers

for num in range (101):
    if num % 2 == 0:
        print(num)

#Use for loop to iterate from 0 to 100 and print only odd numbers
for num in range  (101):
    if num % 2 == 1:
        print(num)
   


#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
total = 0
for num in range (101):
    total += num
    print("the sum of all numbers from 0 to 100 is:", total)


#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

sum_even = 0
sum_odds = 0
for num in range (101):
    if num % 2 == 0:
        sum_even += num
    
    else:
         sum_odds += num 
         
print(" the sum of all numbers from 0 to 100 and the sum of all oods  is:", sum_odds)
print(" the sum of all numbers from 0 to 100 and the sum of all even  is:", sum_even)
   
  