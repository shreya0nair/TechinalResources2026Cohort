n=int(input("Enter a number : "))
if (1<=n<=100):
    for i in range(0,n):
        for j in range(0,i):
            print("  ",end='')
        for k in range(1):
            print("* ",end='')
        for l in range(0,n-i+1):
            print("  ",end='')
        print()
else:
    print("Print number in range.")
