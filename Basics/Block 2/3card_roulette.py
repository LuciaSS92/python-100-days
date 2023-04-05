import random

names_string = input("Give names, separated by comma ")
names = names_string.split(", ")

num_items = len(names)
random_choice = random.randint(0, num_items -1)
pays = names[random_choice]
print(pays)


pays_who = random.choice(names)
print(pays_who)