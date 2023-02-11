#a=input("Enter a number:")
#print (type(a))
#num=int(a)
#print (type(num))
#b=input("Enter a number:")
#print(b)
#print(type(b))
#num1=float(a)
#print(type(num1))

for i in range(1,101):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    if c==2:
        print(i)
   
    
            
    
