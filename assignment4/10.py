'''Program to check if a string contains any special character
Given a string, the task is to check if that string contains any
special character (defined special character set). If any special
character found, don’t accept that string.'''
string=input()
a="!@#$%^&*()-+?_=,<>/"
for i in string:
     if i in a:
         print("string is not accepted")
         break
else:
    print("String is accepted")