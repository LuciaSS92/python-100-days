row1 = ["_", "_", "_"]
row2 = ["_", "_", "_"]
row3 = ["_", "_", "_"]
mapp = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want thetreasure? ")

horizontal = int(position[0]) #2
vertical = int(position[1]) #3

mapp[vertical -1][horizontal -1] = 'X'

print(f"{row1}\n{row2}\n{row3}")