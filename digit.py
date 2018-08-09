count1 = 0
number = int(input("Enter a number "))
while (number > 0):
  number = number//10
  count1 = count1 + 1
print ("Total number of digits : ",count1)
