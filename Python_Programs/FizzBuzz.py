# for number in range(1,101):
#   if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
#   elif number % 3 == 0:
#     print("Fizz")
#   elif number % 5 == 0:
#     print("Buzz")
#   else:
#     print(number)
    
print("Welcome to FizzBuzz!")
Fizz = int(input("Enter a number for fizz :\n"))
Buzz = int(input("Enter a number for buzz :\n"))
print("Here's the solution")
for number in range(1,101):
    if number % Fizz == 0 and number % Buzz == 0:
        print("FizzBuzz")
    elif number % Fizz == 0:
        print("Fizz")
    elif number % Buzz == 0:
        print("Buzz")
    else:
        print(number)
