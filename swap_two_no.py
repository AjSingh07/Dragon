a =67
b = 89
temp = a 
a = b
b = temp
print(a)
print(b)

#without using 3rd variable
a = 67
b = 90
a,b = b,a
print(a,b)