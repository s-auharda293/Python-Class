# my_string = "Hello World from our first Python."
# print(my_string)
# my_string1='''Hello "World"'''
# print(my_string1)
# "our" in my_string
# a="Hello World"
# a in my_string
# #my_list1 = my_list[0::1]
# my_list2=my_list[::-1]
# my_list3=my_list[-1:0:-1]
#check for the number of a and b in the string "aaabcdefaaaabababababaababaabaabbba"


# my_string = "Hello World from our first Python."
# my_st1=my_string[:-1] #goes upto last string
# print(my_st1)
# my_st2=my_string[::-1] #reverses a list
# print(my_st2)
# print(my_string.index("H")) #prints the index where H is located.
# print(my_string.index("Hello")) 
# print(my_string.index(" "))


# name="sauharda khadka"
# print(name.upper())
# print(name.lower())
# print(name.title()) #Capitalizes the first character of each string
# print(name.capitalize()) #Capitalizes the first character of first string  
# print("name1"+" name2") #String Concatenation
# print(name.upper()+" "+name.lower())
# my_string = "Hello World from our first Python."
# print(my_string.index("our")) #prints the first index of letter o in string our
# print(my_string.index("o")) #prints the index of first o it finds
# print(my_string.index("f")) 
# print(my_string.index("first"))


#list splitting
my_string = "Hello World from our first Python."
print(my_string.split(" ")) #every space aauda kheri split garyo 
my_string = "HelloWorld-from-our-first-Python."
print(my_string.split(" "))
print(my_string.split("-"))
my_string = "Hello World from our first Python."
o_binako_list=my_string.split("o") #split and join only work on string
print(o_binako_list)
list_with_o="o".join(o_binako_list)
print(list_with_o) 
o_binako_list1=my_string.split(" ")
adding_list_elements="+".join(o_binako_list1) #adds + to each string 
print(adding_list_elements)

list_stri=str(['Hell', ' W', 'rld fr', 'm ', 'ur first Pyth', 'n.',123])
print(list_stri)
print("+".join(list_stri))

list_stri=(['Hell', ' W', 'rld fr', 'm ', 'ur first Pyth', 'n.',str(123)])
print(list_stri)
print("+".join(list_stri))


