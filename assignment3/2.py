'''to print this pattern
1
22
333
4444
55555
......'''
n=int(input("enter the number grater than 1:"))
for i in range(1,n):
    print(int(i*10**i/9))
