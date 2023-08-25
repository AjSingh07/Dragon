num = eval(input("Enter a number"))
sum = 0
temp = num
while(temp>0):
    d= temp%10
    temp//=10
    sum+=d**3
if num==sum :
      print(num,"Is an Armstrong Number") 
else :
      print(num, "Is not an Armstrong Number")