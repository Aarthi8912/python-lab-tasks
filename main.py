#import task

#a = int(input("Enter first number: "))
#b = int(input("Enter second number: "))

#print("Addition:", task.add(a, b))
#print("Subtraction:", task.subtract(a, b))



def check_palindrome(text):
    if text == text[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"
word = input("Enter a string: ")
result = check_palindrome(word)
print(result)