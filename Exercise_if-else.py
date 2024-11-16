## Exercise If-Else Examples for Beginners

score = int(input("Enter your score: "))
if score > 59:
    print("You passed!")

age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
elif age == 30:
    print("You are in the average age")
else:
    print("You are not in the average age")

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade F")

num = int(input("Enter a number: "))
if num > 0 and num < 10:
    print("The number is a single-digit positive number.")
else:
    print("The number is either negative or has more than one digit.")

number = int(input("Enter a number:"))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

number = int(input("Enter a number: "))
if number >= 0:
    if number == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")
else:
    print("The number is negative.")