a=0
num=int(input("Enter a number to check whether it is perrfect : "))
for i in range(1,num):
    if (num%i==0):
        a=a+i
if (num==a):
    print(num,"is a perfect number")
else:
    print(num,"is not a perfect number")