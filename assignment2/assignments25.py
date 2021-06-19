'''Given a year, determine whether it is a leap year. If it is a leap year, print YES or NO.'''
year=int(input("Enter year="))
if year%4==0 :
    if year%100!=0 :
      print("yes")
    elif year%400==0:
        print("Yes")
    else:print("No")
else:print("No")
