'''
Problem Statement - Design a Calculator, which could calculate the amount 
to be paid individually among the group including the tips. Total Bill,
Tip percentage and number of people are decided by the users.
Solution - 
Suppose to  pay for a bill 10,000 and 10% tips among 6 people would be
bill = 10,000
people = 6
tps rate = 10%
tips = 10% of 10,000
tips = 10/100 X 10,000
tips = 1000
Total to pay :  total = bill + tips
                total = 10,000 + 1000
                total = 11,000
Amount to pay by each individual is :
amount on each = total/people
amount on each = 11,000/6
amount on each = 1,833.33
That's the amount each individual has to pay.

We are done with the problem background. 
So let's start with the programming. 
'''

# First let's print a welcome message indicating tip calculator
print('Welcome to the tip calculator')

'''
Now, take input of total bill amount to be paid
totalBill = input("What was the total bill? : ")
Python automatically decides the datatype and assigns memory implicitly
But when you need a certain datatype, you have to explicitly mention the datatype
Here we're mentioning as float as we're dealing with money.
'''
totalBill = float(input("What was the total bill? : ₹")) 

# Take input of the total number of people to be split among.
totalPpl = int(input("How many people to split the bill? : "))

# input percentage of tip in float 
tipPercent = float(input("What percentage of tip would you consider? 10, 12, 15? : ")) 

'''
now we could proceed from here in two ways,
one way is to create another variable to calculate the tips amount and store the value in it.
then again add it to the total amount and then divide it amoung individuals.
tipsRate = tipPercent / 100
tipAmount = tipsRate * billAmount
totalBill = billAmount + tipAmount
eachBill = totalBill / totalPpl

But, that wasn't what Python was built for
it was built to lessen the code.
that brings us to the other way,
each one's amount = (total + tip) / total people
'''
eachBill = (totalBill + (tipPercent / 100) * totalBill) / totalPpl 

# here, brackets indicate the priority or else it would follow the rule of Precendence

# Now let's print the output
print("The amount each individual has to pay is ₹", eachBill, ".")