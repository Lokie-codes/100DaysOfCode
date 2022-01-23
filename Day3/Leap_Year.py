print(2000%4)
year = int(input("Enter the Year [YYYY] to check if it's a Leap year : "))

def notLeap(year):
    print(year, " is not a Leap year")

def Leap(year):
    print(year, " is a Leap year")

if(year%4 == 0):
    if(year % 100 != 0):
        Leap(year)
        
    else:
        if(year % 400 == 0):
            Leap(year)
        else:
            notLeap(year)
else: 
    notLeap(year)