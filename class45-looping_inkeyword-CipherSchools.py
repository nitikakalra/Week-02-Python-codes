user_info= {
          "name":"nitika",
          "age":19,
          "fav-movies":["3 Idiots","chalk n duster","bahubali"],
          "fav-songs":["mere humsafar","tera yaar hoon main"]
}
if "name" in user_info:
          print("present")
else:
          print("not present")

if "nitika" in user_info.values():
          print("present")
else:
          print("not present")

# for i in user_info


user_info_values=user_info.values()
print(user_info_values)
print(type(user_info_values))



for i in user_info:
          print(i)
user_items=user_info.items()
print(user_items)
print(type(user_items))
for i,j in user_items:
          print(f"keys are {i} and values are {j}")