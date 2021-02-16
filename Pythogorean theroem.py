#importing sqrt(i.e. Square root) from math library

#Pythagoras Theorem 

# c=√a²+b²
# a=√c²-b²
# b=√c²-a²


from math import sqrt
#Hii..This is a program which helps you to find the values using Pythagorean theorem.
print("Hii.... Enter any two values and give  ?  for the value to be find.")

#Getting input value.
x=input("Enter the Adjacent side:")
y=input("Enter the Opposite side:")
z=input("Enter the Hypotenuse side:")

#Here,I have defined two different function since formula for adjacent & opposite side are similar

#calc function is to find both adjacent and opposide side values.
def calc(a,b):
    v=sqrt(a**2-b**2)
    return v

#hcalc function is to find hypotenues side value.
def hcalc(a,b):
    v=sqrt(a**2+b**2)
    return v

while x=="?":
    z=float(z)
    y=float(y)
    #Here i used if statement since y value (i.e. opposite side) can't be larger then Z value(i.e. hypotenuse side)
    if y>z:
        print("Then value of Adjacent side is:",calc(z,y))
    else:
        print("The value of Hypotenuse side is always larger then Opposite side.")
    break

while y=="?":
    z=float(z)
    x=float(x)
    #Here i used if statement since x value (i.e. adjacent side) can't be larger then Z value(i.e. hypotenuse side)
    if x>z:
        print("Then value of Adjacent side is:",calc(z,x))
    else:
        print("The value of Hypotenuse side is always larger then Adjacent side.")
    break

while z=="?":
    x=float(x)
    y=float(y)
    print("Then value of Hypotenuse side is:",hcalc(x,y))
    break
