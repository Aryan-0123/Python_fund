#working with list tuples and dictionaries
my_list = [1, 2, 3]
print(len(my_list))
my_list.append(4)
print(my_list)
my_list.insert(1, 1.5)
print(my_list)
print(my_list.pop())
print(my_list)


tuples = (1, 2, 3)
print(len(tuples))
print(tuples[0])
print(tuples[1:3])
tuples2 = (4, 5, 6)
print(tuples + tuples2)
print(tuples * 2)
print(1 in tuples)
print(4 in tuples)
print(tuples.__dir__())