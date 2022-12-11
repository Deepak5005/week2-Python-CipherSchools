mixed = (1,2,3,4.0)

# for loop and tuple
# for i in mixed:
#     print(i)
# NOTE - You can use while loop to


# tuple with one elements
nums = (1)
words = ('word1',)
# print(type(nums))
# print(type(words))


# tuple without parenthesis
guitars = 'yamaha', 'baton rouge', 'taylor'
# print(type(guitars))



# tuple unpacking
guitarists = ('Maneli Jamal', 'Eddie Van Der Meer', 'Andrew Foy')
guitarist1, guitarist2, guitarist3 = (guitarists)
# print(guitarist1)


# list inside tuples
favorites = ('southern magnolia', ['Tokyo Ghoul Theme', 'landscape'])
favorites[1].pop()
favorites[1].append("we made it")
print(favorites)

# min(), max, sum
print(sum(mixed))