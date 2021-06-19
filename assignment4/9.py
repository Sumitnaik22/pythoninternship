'''Python program to print even length words in a string
Given a string. The task is to print all words with even length in the given string.'''
string=input().split()
for i in string:
    if len(i)%2==0:
        print(i)
