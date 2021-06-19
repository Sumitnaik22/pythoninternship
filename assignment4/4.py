'''Write a program that checks if an array is a hill.
Print "yes" if the given array is a hill. Otherwise, print "no".
it is strictly increasing in the beginning; after that it is constant; after that it is strictly decreasing.
The first block (increasing) and the last block (decreasing) may be absent. It is allowed that both of this
blocks are absent.For example, the following three arrays are a hill: [5,7,11,11,2,1], [4,4,2], [7],
but the following three are not unimodal: [5,5,6,6,1], [1,2,1,2], [4,5,5,6].'''
n=int(input())
a=list(map(int,input().split()))
count=0
state=True
for i in range(0,n-1):
    if a[i]==a[i+1] and state:
        count+=1
        state=False
    elif a[i]<a[i+1] and state and count!=n-2:
        count+=1
    elif a[i]>a[i+1] and not state:
        count+=1
print("Yes" if count==n-1 else "No")