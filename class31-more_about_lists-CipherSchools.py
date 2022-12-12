# numbers=list(range(1,21))
# print(numbers)
# popped_items=numbers.pop()
numbers=[675,4532,543534,543,4532]
# print(numbers.index(4532,2))
def negative_list(l):
          negative=[]
          for i in l:
                    negative.append(-i)
          return negative

print(negative_list(numbers))