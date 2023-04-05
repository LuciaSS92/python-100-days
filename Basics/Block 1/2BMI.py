height = input("Enter height in m: ")
weight = input("Enter weight in kg: ")

bmi = int(weight) / float(height)**2

bmi_int = int(bmi)
print(bmi_int)