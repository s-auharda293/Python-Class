# #can work on tuples and tuples,tuples and list,list and list
# my_list=[1,2,3,4,5]
# next_list = my_list[::-1]
# my_list=[1,2,3,4,5,6,7,8,9,10,11,12]
# def sum_of_num(a,b):
#     return a+b

# print(sum_of_num(1,2))
# sum = map(sum_of_num,my_list,next_list) #my_list,next_list are passed into this map
# print(list(sum))

# # NEW_LIST = []
# # for index in range(len(my_list)):
# #     NEW_LIST.append(my_list[index]+next_list[index])
# # print(NEW_LIST)
 
# jpt_list = list(zip(my_list,next_list)) #jati ota elements bhako lis lai sangai lyaera rakhne milxa
# print(jpt_list)

#passing more arguments to a map
def sum_of_num(a,b,c):
    return a+b+c
my_list=[1,2,3,4,5,6,7]
next_list = my_list[::-1]
my_list1=[1,2,3,4,5,6,7,8,9,10,11,12]
sum = map(sum_of_num,my_list,next_list,my_list1) #my_list,next_list,my_list1 are passed into this map
print(list(sum))
