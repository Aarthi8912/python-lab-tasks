#prime
def is_prime(n):
   if n <= 1:
       return False
   for i in range(2, n):
       if n % i == 0:
           return False
   return True

num = int(input("Enter number: "))
print("Prime Number" if is_prime(num) else "Not Prime")


#fibonacci
def fibonacci(n):
   a = 0
   b = 1
    
   print("Fibonacci Series:")
   for i in range(n):
       print(a, end=" ")
       a, b = b, a + b

num = int(input("Enter number of terms: "))
fibonacci(num)

#modules
import random

print("Random number between 1 and 10:", random.randint(1, 10))
print("Random choice from list:", random.choice([10, 20, 30, 40]))


def add(a, b):
   return a + b

def subtract(a, b):
    return a - b



#zerodivisionerror
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
   print("Error: Cannot divide by zero!")

except ValueError:
   print("Error: Invalid input! Please enter numbers only.")

finally:
   print("Program execution completed.")

#class and object
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def calculate_grade(self):
        if self.marks >= 90:
            return "Grade A"
        elif self.marks >= 70:
            return "Grade B"
        elif self.marks >= 50:
            return "Grade C"
        else:
            return "Fail"
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Result:", self.calculate_grade())
name = input("Enter student name: ")
marks = int(input("Enter marks: "))

s1 = Student(name, marks)
s1.display()