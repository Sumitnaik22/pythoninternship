'''Stubborn Vowels
In english alphabets there are two types of words, vowels and consonents.You are writing
a program to reverse a given string, but the vowels are stubborn to move away from their position.
So given a string where the vowels are stubborn,print what will be word if the entire word is reversed
except for the vowels.'''
s = input()
a = []
l = []
x = 0
status=True

for i in range(len(s)):
    if s[i].lower() in "aeiou":
        a.append(s[i])
        l.append(s[x:i])
        x = i + 1

if s[x:] != "":
    l.append(s[x:])
l.reverse()

rev = ""
if s[len(s)-1].lower() in "aeiou":
    status=False

for i in range(len(l)):
    if i < len(l) and status:
        rev += l[i]
    if i < len(a):
        rev += a[i]
        status=True

print(rev)