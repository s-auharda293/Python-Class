#dictionary comprehension
#of dict.py program
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
item_dict = {key : value + value*0.13 for key,value in price_of_item.items()}
print(item_dict)
item_dict = {f"{key}'s" : value + value*0.13 for key,value in price_of_item.items()} 
#key is string
print(item_dict) 