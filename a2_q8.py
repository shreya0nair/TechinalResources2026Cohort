n=int(input("Enter a number : "))
if (1<=n<=100):
    for i in range(1,n+1):
        for j in range(0,n-i):
            print("  ",end='')
        for k in range(1):
            print("* ",end='')
        for l in range(0,i):
            print("  ",end='')
        print()
else:
    print("Enter number in range.")
