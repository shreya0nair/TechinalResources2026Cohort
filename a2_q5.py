n=int(input("Enter a number : "))
if (1<=n<=100):
    for i in range(1,n//2+2):
        for j in range(0,n//2-i+1):
            print("  ",end='')
        for k in range(1,i+1):
            print("* ",end='')
        for l in range(0,i-1):
            print("* ",end='')
        print() 
    for i in range(1,n//2+1):
        for j in range(0,i):
            print("  ",end='')
        for k in range(1,n//2-i+2):
            print("* ",end='')
        for l in range(0,n//2-i):
             print("* ",end='')
        print()
else:
    print("Enter number in range.")
