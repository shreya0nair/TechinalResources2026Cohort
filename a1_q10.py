n=int(input("Enter a number : "))
print("Prime factors of",n,": ",end='')
if (2<=n<(10**9)):
    for i in range(2,n+1):
        if n%i==0:
            j=1
            for k in range(2,i):
                if i%k==0:
                    j=0
                    break
                else:
                    j=1
            if j==1:
                print(i," ",end='')
else:
    print("Enter number in range")
