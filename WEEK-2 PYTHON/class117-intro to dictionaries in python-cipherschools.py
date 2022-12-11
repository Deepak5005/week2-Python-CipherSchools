# How to create dictionaries
user = {'name' : 'Deepak', 'age' : 20}
print(user)
print(type(user))


# second method to create dictionaries
user1 = dict(name = 'Deepak', age = 20)
# print(user1)

print(user['name'])
print(user['age'])


# which type of data a dictionary can store ?
# anything
# numbers, strings, list , dictionary

user_info = {
    'name' : 'deepak',
    'age' : 20,
    'fav_movies' : ['KGF'],
}
print(user_info)

# How to add to empty dictionary
user_info2 = {}
user_info2['name'] = 'deep'
user_info2['age'] = 20

print(user_info2)
