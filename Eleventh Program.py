# DATE =  11 JANUARY 2023

# VARIABLES
# INPUT
# IF & ELSE
# FOR VOTING
# MATHEMATICAL CONCEPT
# THE RELATIONSHIP BETWEEN SPEED , TIME AND DISTANCE
# RELATED TO SCIENCE


print("---------------------------------<CHECKING YOU CAN VOTE OR NOT>-----------------------------------------")

age = int(input("Enter Your Age:"))
if age >= 18:
    print("YOU CAN VOTE")
else:
    print("YOU CAN NOT VOTE")

print("                                                                                             ")
print("---------------------------------<WHOSE WEIGHT IS MORE>-----------------------------------------")
print("                                                                                             ")

aman = int(input("Enter weight of Aman:"))
jaya = int(input("Enter weight of Jaya:"))

if aman < jaya:
    print("Aman has lesser weight")
else:
    print("Jaya has lesser weight")

print("                                                                                             ")
print("---------------------------------<TRIANGLE>-----------------------------------------")
print("                                                                                             ")

angle1 = int(input("Enter First side:"))
angle2 = int(input("Enter Second side:"))
angle3 = int(input("Enter Third side:"))

if angle1 == angle2 == angle3:
    print("It is an equilateral triangle")
else:
    print("It is not an equilateral triangle")

print("                                                                                             ")
print("---------------------------------<DISTANCE>-----------------------------------------")
print("                                                                                             ")

car1 = int(input("Enter Distance covered by car1 in 1 hour :"))
car2 = int(input("Enter Distance covered by car2 in 1 hour :"))
car3 = int(input("Enter Distance covered by car3 in 1 hour :"))
if car1 > car2:
    if car1 > car3:
        print("Car1 has highest speed")
    else:
        print("Car3 has highest speed")
else:
    if car2 > car3:
        print("Car2 has highest speed")
    else:
        print("Car3 has highest speed")

print("                                                                                             ")
print("---------------------------------<IT'S VOWEL OR CONSTANT>-----------------------------------------")
print("                                                                                             ")

alpha = input("Enter Any Alphabet:")
if alpha == 'a' or alpha == 'e' or alpha == 'i' or alpha == 'o' or alpha == 'u' or alpha == 'A' or alpha == 'E' or alpha == 'I' or alpha == 'O' or alpha == 'U':
    print("It is a Vowel")
else:
    print("It ia a Consonant")

print("                                                                                             ")
print("---------------------------------<IT'S SQUARE OR TRIANGLE>-----------------------------------------")
print("                                                                                             ")

side1 = int(input("Enter The Measure Of Side1 :"))
side2 = int(input("Enter The Measure Of Side2 :"))
if side1 == side2:
    print("It is a Square")
else:
    print("It is a Rectangle")

print("                                                                                             ")
print("---------------------------------<Distance>-----------------------------------------")
print("                                                                                             ")

dis1 = int(input("Enter The Distance Of Home To Market In KM:"))
dis2 = int(input("Enter The Distance Of Home To School In KM:"))
if dis1 < dis2:
    print("Market is Near By Home")
else:
    print("School is Near By Home")

print("                                                                                             ")
print("---------------------------------<Odd or Even>-----------------------------------------")
print("                                                                                             ")

num = int(input("Enter A Number:"))
if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

print("                                                                                             ")
print("---------------------------------<Positive or Negative>-----------------------------------------")
print("                                                                                             ")

num1 = int(input("Enter Any Integer:"))
if num1 > 0:
    print("Number is Positive")
else:
    print("Number is Negative")

print("                                                                                             ")
print("---------------------------------<Who is Largest?>-----------------------------------------")
print("                                                                                             ")

num2 = int(input("Enter First Integer:"))
num3 = int(input("Enter Second Integer:"))
if num2 > num3:
    print("First Integer Is Largest")
else:
    print("Second Integer Is Largest")

print("                                                                                             ")
print("---------------------------------<Without Entering>-----------------------------------------")
print("                                                                                             ")

num4 = 90
num5 = 100
if num4 > num5:
    print("num4 is largest")
else:
    print("num4 is largest")

print("                                                                                             ")
print("---------------------------------<Relational Operator - 1(Greater Than And Less Than )>-----------------------")
print("                                                                                             ")

num6 = 10
num7 = 20
print(num6 > num7)

num6 = 10
num7 = 20
print(num6 < num7)

print("                                                                                             ")
print("----------------<Relational Operator - 2(Greater Than Or Equal To And Less Than Or Equal To )>------------------")
print("                                                                                             ")

num8 = 50
num9 = 30
print(num8 >= num9)

num10 = 50
num11 = 30
print(num10 <= num11)

print("                                                                                             ")
print("----------------<Relational Operator - 3( Equal To And Not Equal To )>------------------")
print("                                                                                             ")

num12 = 70
num13 = 80
print(num12 == num13)

num12 = 70
num13 = 80
print(num12 != num13)

print("                                                                                             ")
print("---------------------------------<Arithmatic Operator - 1(Addition And Concatenation)>-----------------------")
print("                                                                                             ")

a = 200
b = 45
print(a + b)

a1 = 'Good'
b2 = 'Morning'
print(a1 + " " + b2)

print("                                                                                             ")
print("---------------------------------<Arithmatic Operator - 2(Subtraction)>-----------------------")
print("                                                                                             ")

c = 90
d = 10
print(c - d)

print("                                                                                             ")
print("---------------------------------<Arithmatic Operator - 3(Multiplication And Replication)>-----------------------")
print("                                                                                             ")

e = 4
f = 5
print(e * f)

e1 = "python "
print(e1 * 3)


print("                                                                                             ")
print("---------------------------------<Arithmatic Operator - 4(Division)>-----------------------")
print("                                                                                             ")

g = 28
h = 4
print(g / h)

print("                                                                                             ")
print("---------------------------------<Arithmatic Operator - 5(Floor Division)>-----------------------")
print("                                                                                             ")

i = 20
j = 5
print(i // j)

i1 = 40
j2 = 3
print(i1 // j2)  # here we don't get numbers after decimal

print("                                                                                             ")
print("---------------------------------<Arithmatic Operator - 6(Remainder)>-----------------------")
print("                                                                                             ")

k = 67
o = 9
print(k % o)   # here we get the remainder

print("                                                                                             ")
print("---------------------------------<Arithmatic Operator - 7(Exponents)>-----------------------")
print("                                                                                             ")

m = 8
n = 2
print(m ** n)  # here we got 8*8

print("                                                                                             ")

o = ">>>"
t = "HERE"
u = "THE"
v = "CODE"
w = "IS"
x = "OVER"
p = "<<<"
print(o, t, u, v, w, x, p)

g7 = ">>>"
a1 = "BYE!!"
b2 = "HAVE"
c3 = "A"
d4 = "NICE"
e5 = "DAY"
f6 = "<<<"
print(g7, a1, b2, c3, d4, e5,side)
