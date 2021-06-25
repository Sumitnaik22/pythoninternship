
def prime_number(i):   #to check property
 for j in range(2,i):
    for k in range(2,(j//2+1)):
        if j%k==0:
            break
    else:y.append(j)
    if sum(y)==i:
        x.append(i)
        break
    elif sum(y)>i:
        return
n=int(input())  # getting input
x=[]
for i in range(3,n+1):   #finding prime number btw 3 to N
    for m in range(2,i):
        y=[]
        if i%m==0:
            break
    else:
        prime_number(i)
print(*x,sep=" ")  # print numbers with given property