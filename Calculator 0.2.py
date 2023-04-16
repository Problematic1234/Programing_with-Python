# DATE = 31 DECEMBER 2022

# if ,else,elif

num1 = int(input("enter first no. :"))
num2 = int(input("enter second no. :"))
num3 = int(input("enter third no. :"))
num4 = int(input("enter fourth no. :"))
num5 = int(input("enter fifth no. :"))
op = input("enter operator :")
if op == '+':
    print("your sum is:", num1+num2+num3+num4+num5)
elif op == '-':
    print("your difference is:", num1-num2-num3-num4-num5)
elif op == '*':
    print("your product is:", num1*num2*num3*num4*num5)
elif op == '/':
    print("your division is:", num1/num2/num3/num4/num5)
elif op == '+,-,*,/':
    print("your answer is:", num1+num2-num3*num4/num5)
elif op == '/,*,-,+':
    print("your answer is:", num1/num2*num3-num4+num5)
elif op == '-,+,/,*':
    print("your answer is:", num1-num2+num3/num4*num5)
elif op == '*,/,-,+':
    print("your answer is:", num1*num2/num3-num4+num5)
elif op == '*,-,/,+':
    print("your answer is:", num1*num2-num3/num4+num5)
elif op == '+,/,-,*':
    print("your answer is:", num1+num2/num3-num4*num5)
elif op == '+,*,-,/':
    print("your answer is:", num1+num2*num3-num4/num5)
elif op == '/,-,*,+':
    print("your answer is:", num1/num2-num3*num4+num5)
elif op == '+,/,-,*':
    print("your answer is:", num1+num2/num3-num4*num5)
elif op == '+,*,/,-':
    print("your answer is:", num1+num2*num3/num4-num5)
elif op == '-,/,*,+':
    print("your answer is:", num1-num2/num3*num4+num5)
elif op == '/,*,-,/':
    print("your answer is:", num1/num2*num3-num4/num5)
elif op == '/,-,*,/':
    print("your answer is:", num1/num2-num3*num4/num5)
else:
    print(" sorry not entered in the data")
