def division(a,b):
          try:
                    return a/b
          except ZeroDivisionError as err:
                    print(err)
          except TypeError as err:
                    print("Numbers must be Zero")
          except  :
                    print("unexpected error")
print(division(23,78))
          