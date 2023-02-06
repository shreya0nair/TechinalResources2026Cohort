n=int(input("Enter a number : "))
if (1<=n<=10):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)
    print()
else:
    print("Enter number in range.")
