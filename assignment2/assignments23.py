'''Write a program to calculate the EB Bill.
The tariff rate for all division is the same. Karnataka electricity board single slaps for the
domestic LT supply such as for 0 to 30 units the per-unit cost will be ? 3.75/-, from 31 to 100
the per-unit cost will be ? 5.20, from 101 to 200, the per-unit cost will be ? 6.75 and above
201 units you have to pay ? 7.8 per unit.Additionally, the consumer will pay fixed charges as
60/- and electricity tax of 5% extra.'''
unit=int(input("Enter units of electricity consumed="))
if 0<=unit<31:
     bill=3.75*unit
elif 30<unit<101:
     bill=5.2*unit
elif 100<unit<201:
     bill=6.75*unit
else:
     bill=7.8*unit
tax=0.5*bill
total=bill+tax+60
print("Totl bill=",total)