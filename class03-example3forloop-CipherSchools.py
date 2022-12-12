name=input("enter your name: ")
temp=""
for i in range(0,len(name)):
          if name[i] not in temp:
                    print(f"{name[i]}: {name.count(name[i])}")
                    temp=temp+name[i]
          
name=input("enter a number: ")
none=""
for i in range(0,len(name)):
          if name[i] not in none:
                    print(name[i] ,":",name.count(name[i]) )

