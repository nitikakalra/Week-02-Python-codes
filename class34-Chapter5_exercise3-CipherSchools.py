def revarse_element(a):
          element=[]
          for i in a:
                    element.append(i[::-1])
          return element
alpha=["abc","tuv","xyz"]
print(revarse_element(alpha))
