print("Welcome to the food ordering Chatbot")
name = input("What is your name? ")
age = int(input("Hello " + name + ", how old are you? "))
print(str(age) + ". Nice! Now, how can I be of your assistance today? ")

while True:
    print("1. View the Menu.")
    print("2. Place an order")
    print("3. Track your order")
    print("4. Exit ")

    choice = input("Please enter the number of your choice. ")
    
    if choice == "1":
        print("We have Hamburgers, Tacos, and French Fries.")
    elif choice == "2":
        print("Let's place an order.")
    elif choice == "3":
        print("Let's track your order.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Sorry. That's not an option, try again!")
