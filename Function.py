def greater(a,b):
    if a>b :
        print("A is greater")
    else:
        print("B is greater")
a = eval(input("Enter a number"))
b=  eval(input("Enter b number"))
greater(a,b)

def average(*number):
    sum =0 
    for i in number :
        sum = sum + i
    return sum/len(number)
    
    
c = average(5,5,5,5,10)
print(c)