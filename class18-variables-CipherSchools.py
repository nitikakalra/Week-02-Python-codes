x=5 #global variables
def function():
          global x
          x=7 #local variables
          return x
print(function())
print(x)