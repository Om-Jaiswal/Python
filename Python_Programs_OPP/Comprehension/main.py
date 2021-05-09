numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# List Comprehension-1
squared_numbers = [num**2 for num in numbers]
print(squared_numbers)

# List Comprehension-2
result = [num for num in numbers if num % 2 == 0]
print(result)

# List Comprehension-3
with open("file1.txt") as file1:
  file_1_data = file1.readlines()

with open("file2.txt") as file2:
  file_2_data = file2.readlines()

output = [int(num) for num in file_1_data if num in file_2_data]

print(output)

# Dictionary Comprehension-1
sentence = "what is the Airspeed Velocity of an Unladen Swallow?"

result = {word:len(word) for word in sentence.split()}

print(result)

# Dictionary Comprehension-2
weather_c = {
  "Monday": 12,
  "Tuesday": 14,
  "Wednesday": 15,
  "Thursday": 14,
  "Friday": 21,
  "Saturday": 22,
  "Sunday": 24,
}

weather_f = {day:(temp_c*9/5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)
