# practice for loop
# ask user name and count each character
# "Deepak Kumar Singh"
# D : 1
# e : 2
# p : 1
# a : 2
# k : 2
# u : 1
# m : 1
# r : 1
# S : 1
# i : 1
# n : 1
# g : 1
# h : 1
#   : 2
name = input("enter your name : ")
temp = ""
for i in range(0, len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp += name[i]