price_of_item = {
            'apple': 120,
            'banana': 330,
            'orange': 210,
            'pear': 210,
            'grape': 410,
            'pineapple': 560,
            'strawberry': 770,
            'watermelon': 660
}
#Method-1
# my_dict=price_of_item
# for key,value in price_of_item.items():
#     my_dict[key] = value + (13/100)*value 
# print(my_dict)
# price_of_item = my_dict

#Method-2
# item_dict={}
# for key,value in price_of_item.items():
#       item_dict[key] = value + (13/100)*value
# print(item_dict)

#Method-3 
#using update
for key,value in price_of_item.items():
      value = value + (13/100)*value
      price_of_item.update({key : value})
print(price_of_item)
