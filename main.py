my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(type(my_list))
# print list
print(my_list)

# print list ascendent order
print(sorted(my_list))

# print list descendent order
print(sorted(my_list, reverse=True))

# sort for slice
my_list = (sorted(my_list))
print(my_list)

# print even num
even_my_list = my_list[1::2]
print(even_my_list)
# print odd num
odd_list = my_list[::2]
print(odd_list)

# print mult of 3
trd_list = my_list[2:9:3]
print(trd_list)
