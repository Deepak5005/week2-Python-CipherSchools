# add and delete data
user_info = {
    'name' : 'deepak',
    'age' : 20,
    'fav_movies' : ['KGF'],
}

# How to add data
user_info['fav_movies'] = ['movie1', 'movie2']
print(user_info)



# pop method
popped_item = user_info.pop('fav_movies')
print(f"popped item is {popped_item}")
print(user_info)



# popitem method
popped_item = user_info.popitem()
print(user_info)
print(popped_item)
print(type(popped_item))
