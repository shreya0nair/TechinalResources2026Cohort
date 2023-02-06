n=int(input("Enter a number : "))
if (1<=n<=5):
    first=1
    second=1
    print(0)
    print(str(first)+"  "+str(second))
    for i in range(3,n+1):
       for j in range(1,i+1):
           c=first+second
           print(str(c)+"  ",end='')
           first,second=second,c
       print()
else:
    print("Enter number in range.")

