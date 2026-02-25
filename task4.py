#Factorial
num = int(input("Enter a number: "))
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1

print("Factorial:", fact)


#Check leap year
year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
   print("Not a Leap Year")


#calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
   print("Result:", a + b)
elif op == "-":
   print("Result:", a - b)
elif op == "*":
   print("Result:", a * b)
elif op == "/":
  print("Result:", a / b)
else:
   print("Invalid Operator")



#count vowels
text = input("Enter a string: ")
count = 0

for ch in text.lower():
  if ch in "aeiou":
      count += 1

print("Number of vowels:", count)


#palindrome
text = input("Enter a string: ")

if text == text[::-1]:
   print("Palindrome")
else:
   print("Not Palindrome")



#Remove duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]

unique = list(set(numbers))

print("List without duplicates:", unique)



#count occurrence
numbers = (1, 2, 3, 2, 4, 2)

print("Count of 2:", numbers.count(2))


#Union andintersection
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)

marks = {"Math": 80, "Science": 75}

marks["English"] = 90     # Add
marks["Math"] = 85        # Update

print("Updated Dictionary:", marks)

marks = {"Math": 80, "Science": 75, "English": 90}

total = sum(marks.values())

print("Total Marks:", total)



set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

difference = set1 - set2

print("Set 1:", set1)
print("Set 2:", set2)
print("Difference (set1 - set2):", difference)


numbers = {10, 15, 22, 33, 40, 55}
even_numbers = set()
for num in numbers:
   if num % 2 == 0:
       even_numbers.add(num)

print("Original Set:", numbers)
print("Even Numbers:", even_numbers)



numbers = set()
n = int(input("How many elements? "))

for i in range(n):
    value = int(input("Enter element: "))
    numbers.add(value)

max_value = None

for num in numbers:
    if max_value is None or num > max_value:
        max_value = num

print("Maximum value:", max_value)