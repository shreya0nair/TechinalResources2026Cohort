n=int(input("Enter a number : "))
if (1<=n<=100):
    for i in range(1,n+1):
        for j in range(1,n-i+2):
            print("* ",end='')
        print()
else:
    print("Enter number in range")
