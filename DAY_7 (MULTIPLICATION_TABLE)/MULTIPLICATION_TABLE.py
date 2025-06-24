# To get the table required from the user
num =int(input("Enter a number for which the table to be built : "))

# To get the last digit of a table required from the user
last=int(input("Enter the last multiplier : "))

# Iterate n times from i = 1 to last+1
for i in range(1, last+1):
   print(num, 'x', i, '=', num*i) 
# Printed the required table
