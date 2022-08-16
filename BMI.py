a = int(input("height in cm : "))
b = int(input("Weight in kg : "))
c = (a/100)**2
d = b/c


if 19 <= d <= 24.99:
    print("normal")

elif 25<= d <= 29 :
    print("overweight")

elif 30 <= d <= 34 :
    print("obese")

elif 35 < d :
    print("extremely obese")

elif d<18 :
    print("underweight")