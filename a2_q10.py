n=int(input("Enter a number : "))
if (1<=n<=100) and (n%2!=0):
    for i in range(1,n//2+2):
        for j in range(0,n//2-i+1):
            print("  ",end='')
        for k in range(1):
            print("* ",end='')
        for l in range(0,2*i-3):
            print("  ",end='')
        if i!=1:
            for m in range(1):
                print("* ",end='')
        print()
    for i in range(1,n//2+1):
        for j in range(1,i+1):
            print("  ",end='')
        for k in range(1):
            print("* ",end='')
        if i!=(n//2):
            for l in range(1,2*(n//2)-2*i):
                print("  ",end='')
        if i!=(n//2):
            for m in range(1):
                print("* ",end='')
        print()
else:
    print("Enter odd number in range.")
    
