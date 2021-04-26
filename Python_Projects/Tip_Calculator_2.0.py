import random

def tip_calculator():
    print("__________________________________________________")
    print("\nWelcome to the tip calculator!")
    
    bill = float(input("What was the total bill? \n$"))
    tip = int(input("How much tip would you like to give(5%, 10% or 15%)?\n"))
    people = int(input("How many people to split the bill?\n"))
    
    tip_as_percent = tip / 100
    total_tip_amount = bill * tip_as_percent
    total_bill = bill + total_tip_amount
    bill_per_person = total_bill / people
    final_amount = round(bill_per_person, 2)
    final_amount = "{:.2f}".format(bill_per_person)
    
    print(f"Each person should pay ${final_amount}")

def who_will_pay():
    print("__________________________________________________")
    names_string = input("\nGive me everybody's names, seperated by a comma: \n")
    
    names = names_string.split(",")
    num_items = len(names)
    random_choice = random.randint(0, num_items-1)
    person_who_will_pay = names[random_choice].title()

    #person_who_will_pay = random.choice(names)

    print(person_who_will_pay + " is going to buy the meal today!")

def start():
    print("__________________________________________________")
    print("\nWhat would you like to do?\n1.Calculate tip\n2.Guess who will pay")
    choice = int(input("Enter a choice(1/2): "))
    if choice == 1:
        tip_calculator()
    elif choice == 2:
        who_will_pay()
    else:
        print("Invalid Choice")

start()

would_continue = True
while would_continue:
    print("__________________________________________________")
    ask = input("\nWould you like to continue(Yes/No)?\n").title()
    if ask == "Yes":
        start()
    elif ask == "No":
        would_continue = False
        print("Thank you!")
    else:
        print("Invalid Choice")
