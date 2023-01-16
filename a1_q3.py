t=int(input("Enter count of input numbers to be tested : "))
if (1<=t<=10001):
    for n in range(t):
        n=int(input("Enter number : "))
        if (2<=n<=(10**9)):
            for i in range(2,n):
                if (n%i)==0:
                    print("not prime")
                    break
            else:
                print("prime")
        else:
            print("Enter number in range")
else:
    print("Enter number in range")
