dictionary_1 = { 'a': 1, 'b': 2, 'c': 3, 4:5}
print(dictionary_1)
dictionary1 = { 'a': 1, 'b': 2, 'c': None} # key and value pair
print(dictionary1)                         
# print("the value of the first element:",dictionary1['a']) 
# print("the value of the second element:",dictionary1[4])
# print("the length of the dictionary:",len(dictionary1))
# print("the values in dictionary:",dictionary1.values())
# print("The type of dictionary values:",type(dictionary1.values())) 
# print("the keys in dictionary:",dictionary1.keys())
# print("The type of key values:",type(dictionary1.keys())) 
for key, value in dictionary1.items():
    print(key,value)
for key, value in dictionary_1.items():
    print(key,value)
dictionary1 = { 'a': 1, 'b': 2, 'c': None}
for key in dictionary_1.items():
    print(key)


