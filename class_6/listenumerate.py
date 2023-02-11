# my_string = "Hello world from python script"
# my_list = my_string.split(" ")
# print(my_list)
# for index,item in enumerate(my_list): #gives index of individual word
#     print (index,item)
#     if index %2 == 0:
#         my_list[index] = item.upper()
# print(my_list)


##alternate method
c=0
my_string = "Hello world from python script"
for i in my_string:
    if i==" ":
        d=c+1
        do
          my_string[d] = my_string.upper()
          d=d+1
        while my_string[d] == " "   

c=c+1


#list comprehension
my_list=[my_str]
b = [item.upper() for item in my_list if my_list.index(item % 2 == 0)]
print(b)