'''PATTERN AS SHOWN IN SAMPLE TEST CASE
for N=5
1
 2
  3
   4
    5
    '''
n=int(input("Enter a  number:"))
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            print(i+1,end=" ")
        else:
            print("",end=" ")
    print()

