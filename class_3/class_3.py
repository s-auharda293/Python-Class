#write a number to check a number is palindrome or not using functions
def check_palindrome(num):
    temp=num
    rev=0
    while num!=0:
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if temp==rev:
        return True
    else: 
        return False
num=int(input("Enter a number:"))
if check_palindrome(num):
    print("The number is a palindrome!")
else:
    print("The number is not palindrome.")
