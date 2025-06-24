num=int(input("Enter a number to check whether it is prime or not : "))
count=0
for i in range (1,num):
    if (num%i==0):
        count+=1
if count>2:
    print("The number",num,"is not a Prime number")
else:
    print("The number",num,"is a Prime number")