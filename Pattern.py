rows = eval(input("ENter the number of Rows"))
for i in range(rows,0,-1) :
    for j in range(i,rows+1):
        print(i,end ='')
    print('')
    
# For Normal star Pattern

row =int(input("Enter the no of rows"))
for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end='')
    print('')