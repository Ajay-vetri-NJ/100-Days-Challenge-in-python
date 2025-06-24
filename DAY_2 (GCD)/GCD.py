def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
#getting values form the user
a=int(input("Enter a value for A : "))
b=int(input("Enter a value for B : "))
#Assigning according to a value
Gcd=gcd(a,b)
print("The gcd for the given inputs ",a,"and",b,"are : ",Gcd)