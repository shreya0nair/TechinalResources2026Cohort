n=int(input("Enter a number : "))
if (1<=n<=10):
    for i in range(1,n+1):
       for j in range(0,n-i+1):
        print("  ",end='')
       for j in range(1,i+1):
        print("* ",end='')
       print()
else:
    print("Enter number in range")
