age = input("What is your current age? ")

years = int(age)

months = years * 12
weeks = years * 52
days = years * 365
years_remaining = 90 - years

message = f"Your age in years is {years}, in weeks {weeks}, and in days {days}\nYou have {years} years left to live."
print(message)