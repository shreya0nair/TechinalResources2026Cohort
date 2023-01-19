n=int(input("Enter a number : "))
if (1<=n<(10**8)):
    inv=0
    j=1
    while n>0:
        i=int(n%10)
        d=int(j)
        p=int(i)
        n=int(n/10)
        inv=inv+int(j*(10**(i-1)))
        j+=1
    print("Inverse : ",inv)
else:
    print("Enter number in range")
