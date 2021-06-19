'''Read four integers from the keyboard a,b,c, d and those values in the following order.
max > mid1 > mid2 > min(using if else statements)'''
a,b,c,d=map(int,input().split())

if b>a:
    count=a
    a=b
    b=count
if d>c:
    count=c
    c=d
    d=count
if a>c:
    max=a
    if b>d:
     min=d
     if b>c:
          mid1=b
          mid2=c
     else:
          mid1=c
          mid2=b
    else:
      min=b
      mid1=c
      mid2=d
else:
    max=c
    if b>d:
      min=d
      mid1=a
      mid2=b
    else :
      min=b
      mid1=d
      mid2=a
print(max,mid1,mid2,min,sep=">")
