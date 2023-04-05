import random

random_interger = random.randint(1, 10)
print(random_interger)


random_float = random.random() #betwn 0 and 0.9999
# * 5 betwn 0 and 4.9999
print(random_float)

love_score = random.randint(1, 100)
print(love_score)


random_side = random.randint(0, 1)
if random_side ==1:
    print("Heads")
else:
    print("Tails")