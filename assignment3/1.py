'''At the idli shop there are two types of Rava Idli's available.
One goes for Rs.A per piece and the other goes for Rs.B per piece.
The girl has a total of K rupees.
What is the maximum number of rava idlis that she can have'''
n=int(input("Enter the number of cases:"))
for i in range (0,n):
    a,b,k=map(int,input("Enter values of A,B and K:").split())
    m=k//a
    l=k//b
    print(max(m,l))
