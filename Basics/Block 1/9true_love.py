print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

combine_string = name1 + name2
lower_string = combine_string.lower()

t = lower_string.count("t")
r = lower_string.count("r")
u = lower_string.count("u")
e = lower_string.count("e")
true = t+r+u+e

l = lower_string.count("l")
o = lower_string.count("o")
v = lower_string.count("v")
e = lower_string.count("e")
love = l+o+v+e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your loves score is {love_score}, you go together like coke and Mentos")
    
elif (love_score >=40) and (love_score <=  50):
    print(f"Your loves score is {love_score}, you are alright together. ")
else:
    print(f"Your loves score is {love_score}")


