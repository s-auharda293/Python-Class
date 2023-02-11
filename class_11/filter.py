# new_list = [1,2,3,4,5,6,7,8,9,10]
# def odd_even(b):
#     if b%2==0:
#         return True
#     else:
#         return False
# my_list = list(filter(odd_even,new_list))
# print(my_list)
new_list = [1,2,3,4,5,6,7,8,9,10]
new_list = list(filter(lambda x : x%2==0,new_list))
print(new_list)