'''Check if a Substring is Present in a Given String
Given two strings, check if s1 is there in s2.'''
s1=input()
s2=input()
m=s2.find(s1)
print("Yes" if m!=-1 else "No")