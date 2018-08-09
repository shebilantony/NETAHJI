num01 = 10
num02 = 14
num03 = 12
if (num01 >= num02) and (num01 >= num03):
   largest = num01
elif (num02 >= num01) and (num02 >= num03):
   largest = num02
else:
   largest = num03

print("The largest number between",num01,",",num02,"and",num03,"is",largest)
