'''Read three integers from the keyboard a,b,c and those values
in the following order.
max > mid > min'''
a,b,c=map(int,input().split())
m=max(a,b,c)
n=min(a,b,c)
mid=a+b+c-(m+n)
print(m,">",mid,">",n,)