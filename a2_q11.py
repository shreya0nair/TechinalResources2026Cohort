n=int(input("Enter a number : "))
x=1
if (1<=n<=44):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(str(x)+" ",end='')
            x+=1
        print()
else:
    print("Enter number in range.")
