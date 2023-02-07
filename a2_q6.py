n=int(input("Enter a number : "))
if (1<=n<=100) and (n%2!=0):
    for i in range(1,n//2+2):
        for j in range(1,n//2-i+3):
            print("* ",end='')
        for k in range(1,2*i):
            print("  ",end='')
        for o in range(1,n//2+3-i):
            print("* ",end='')
        print()
    for l in range(1,n//2+1):
        for m in range(1,l+2):
            print("* ",end='')
        for n in range(1,2*(n//2)):
            print("  ",end='')
        for p in range(1,l+2):
            print("* ",end='')
        print()
else:
    print("Enter number in range.")
