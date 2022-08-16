fname = input("your first name :")
lname = input("your last namev :")
a = float(input("The grade of the first lesson :"))
b = float(input("The grade of the second lesson :"))
c = float(input("the grade of the third lesson :"))
average = (a+b+c)/3
if 12 <= average < 17:
    print( fname , lname , "is educational status : Normal")

elif average< 12 :
    print( fname , lname , "is educational status : Fail")

elif average >= 17 :
    print( fname , lname , "is educational status : Great")
