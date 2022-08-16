import math
a = float(input("first nomber : "))
b = float(input("second nomber : "))

d = input("the operation ? : ")

if d =="+" :
    print(a+b)

if d == "-":
    print(a-b)
    
if d == "*":
    print(a*b)
    
if d == "/":
    if b == 0 :
        print("wrong")
    else :
        print(a/b)

if d == "radical" :
    print(math.sqrt(a))

if d == "sin" :
    print(math.sin(a/(180/math.pi)))

if d == "cos" :
    print(math.cos(a/(180/math.pi)))

if d == "tan" :
    print(math.tan(a/(180/math.pi)))

elif d == 'cot' :
    print(math.cot(a/(180/math.pi)))

elif d == 'factoriel' :
    print(math.factorial(a))

