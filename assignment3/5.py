'''PRINT THE BELOW MENTIONED PATTERN FOR ANY "N" VALUE. WHERE "N" INDICATES NO.OF ROWS.
N is only odd
for N=5
1   5
 2 4
  3
'''
n=int(input())
for i in range(1,(n+1)//2):
    print(" "*(i-1),i," "*(n-2*i),n+1-i)
print(" "*(n//2+1),n//2+1)
