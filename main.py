print("Welcome to the food ordering Chatbot")
name = input("What is your name? ")
age = int(input("Hello " + name + ", how old are you? "))

if age >= 18:
    print("You qualify for the full menu! ")
elif age <= 18:
    print("You qualify for the kid's menu! ")