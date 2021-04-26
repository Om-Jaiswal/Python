student_scores = input("Input a list of student scores:\n").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print("\nList of scores: " + str(student_scores))

# lowest_score = min(student_scores)
# highest_score = max(student_scores)

lowest_score = student_scores[0]
for score in student_scores:
  if score < lowest_score:
    lowest_score = score
print(f"The lowest score in the class is {lowest_score}")

highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f"The highest score in the class is {highest_score}")