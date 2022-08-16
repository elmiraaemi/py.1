a = int(input("The first angle of the triangle :"))
b = int(input("The second angle of the triangle :"))
c = int(input("The third angle of the triangle :"))
if a<b+c and b<a+c and c<a+b : 
    print("Right")
else :
    print("wrong")