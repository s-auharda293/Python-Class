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
#below are user defined functions
#Method -1
# def get_price_of_items(price_of_item,tax_rate):
#     return {key : value + value*tax_rate for key,value in price_of_item.items()}
# print(get_price_of_items(price_of_item,0.13))

# #Method -2 Using default arguments
# def get_price_of_items(price_of_item,tax_rate=0.13):
#     return {key : value + value*tax_rate for key,value in price_of_item.items()}
# print(get_price_of_items(price_of_item))

#changing the value of taxrate to 15 percent
# def get_price_of_items(price_of_item,tax_rate=0.15):
#     return {key : value + value*tax_rate for key,value in price_of_item.items()}
# print(get_price_of_items(price_of_item))

#examples of built in functions are append,update,pop...etc

#create a function which takes i/p a real number 
#returns it's functional value 
def get_functional_value(x):
    return x*x+5*x+1
x = input("Enter a number:")
print(get_functional_value(int(x)))
