""" Some prime numbers can be expressed as a sum of other consecutive prime numbers.
For example

5 = 2 + 3,

17 = 2 + 3 + 5 + 7,

41 = 2 + 3 + 5 + 7 + 11 + 13.

Your task is to find out how many prime numbers which satisfy this property are present in the range 3 to N 
subject to a constraint that summation should always start with number 2.
Write code to find out the number of prime numbers that satisfy the above-mentioned property in a given range.

Input Format: First line contains a number N

Output Format: Print the total number of all such prime numbers which are less than or equal to N.
"""
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
