def lcm(a,b):

#to choose the greatest number
    if (a<b):
        high=a 
    else:
        hgh=b
        
    #To check the main condition
    while(True):
        if((high%a==0) and (high%b==0)):
            lcm=high
            break
        high=high+1
    return lcm

#To get the inputs from the user
num1=int(input("Enter the first number : "))
num2=int(input("Enter the Second number : "))


#Printing the final output
print("The L.C.M of",num1," and ",num2,"is :",lcm(num1,num2))