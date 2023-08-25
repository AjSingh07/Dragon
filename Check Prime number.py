n=6
if n>1:
 for i in range(2,int(n/2)+1):
    if(n%i)==0:
        print(n,"Is not a prime number")
        break
    else:
        print("prime number")
else:
    print("Not a prime number")
        