# total = 0
# for number in range(1,101):
#   total += number
# print("Sum of numbers, range from 1-100 is " + str(total))

# total = 0
# for number in range(2,101,2):
#   total += number
# print("Sum of even numbers, range from 1-100 is " + str(total))

total = 0
for number in range(1,101):
  if number % 2 == 0:
    total += number
print("Sum of even numbers, range from 1-100 is " + str(total))