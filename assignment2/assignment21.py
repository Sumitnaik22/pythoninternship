'''Given an integer,n, perform the following conditional actions:
If n is odd, print Weird
If n is even and
    in the inclusive range of 2 to 5, print Not Weird
    If n is even and in the inclusive range of 6 to 20, print Weird
    If n is even and greater than 20, print Not Weird'''
n=int(input("Enter a number in between 1 and 100:"))
if n%2!=0:
    print("Weird")
elif n in range(2,6):
    if n%2==0:
        print("Not weird")
elif n in range(6,21):
    if n%2==0:
        print("Wierd")
elif n>20:
    if n%2==0:
        print("Not Weird")