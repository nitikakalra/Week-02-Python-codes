def greater(a,b,c):
          if a>b and a>c:
                    return a
          elif b>a and b>c:
                    return b
          else:
                    return c
num1=int(input("enter the very first number: "))
num2=int(input("enter the second number: "))
num3=int(input("enter the thrd number: "))
print(greater(num1,num2,num3),"is the greatest of the whole numbers")