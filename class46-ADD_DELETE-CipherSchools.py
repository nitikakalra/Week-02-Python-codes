user_info= {
          "name":"nitika",
          "age":19,
          "fav-movies":["3 Idiots","chalk n duster","bahubali"],
          "fav-songs":["mere humsafar","tera yaar hoon main"]
}


user_info["fav-tunes"]=["dosti"]
print(user_info)
user_pop=user_info.pop("fav-movies")
print(user_info)

popped_items=user_info.pop("fav-songs")
print(type(popped_items))
print(popped_items)

