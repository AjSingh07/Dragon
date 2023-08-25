num = eval(input("Enter a number"))
fact =1
ans =1
while fact<=num :
  ans = ans*fact
  fact= fact+1
print("Factorial of given number is",ans)

num = eval(input("Enter a number"))
sum = 0
temp = num
while(temp>0):
    d= temp%10
    temp//=10
    sum+=d**3
if temp==sum :
      print(temp,"Is an Armstrong Number") 
else :
      print(temp, "Is not an Armstrong Number")