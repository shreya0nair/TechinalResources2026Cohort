num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))
n1=num1
n2=num2
if (2<=n1<=(10**9)) and ((2<=n2<=(10**9))):
    while (num1%num2)>0:
        rem=num1%num2
        num1=num2
        num2=rem
    gcd=int(num2)
    lcm=(n1*n2)//gcd
    print("gcd of",n1,"and",n2,":",gcd)
    print("lcm of",n1,"and",n2,":",lcm)
else:
    print("Enter number in range")
