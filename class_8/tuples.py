# #looping in tuple:
# my_tuple = (1,2,3)
# for i in my_tuple:
#     print(i)
my_tuple = (1,2,3,"hello")
for i in my_tuple:
    print(i)
#my_tuple.pop() 
print(my_tuple)


#if we have to change elements in a tuple:
my_list = list(my_tuple)
my_list.append(123)
#print(my_list.append(1)) #adds 1 at the end of the list and also returns value none of my_list.append(1)
tup = tuple(my_list)
print(tup)
print(tup.count(1)) #counts the number of 1's in tuple


