height = float(input("How tall are you(in meters)? "))
bill = 0

if height >= 120:
    print("You can ride the rolleroaster!")
    age = int(input("How old are you? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif age >= 45 and age <=55:
        print("Everything is going to be okk. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12")
        
    photo = input("Do you want a photo taken? Y or N. ").upper()
    if photo == "Y":
        bill += 3
        print(f"Your final bill is {bill}")
    else:
        bill
        print(f"Your final bill is ${bill}")
        
else:
    print("Sorry, you have to grow taller before you can ride")
    
