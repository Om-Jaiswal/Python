age = input("What is your current age?\n")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_reamining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_reamining} days, {weeks_remaining} weeks and {months_remaining} months left."

print(message)