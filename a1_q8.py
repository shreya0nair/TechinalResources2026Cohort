n=int(input("Enter a number : "))
k=int(input("Enter number of times to be rotated : "))
if (1<=n<(10**9)) and (-(10**9)<k<(10**9)):
    temp=int(n)
    j=0
    while temp>0:
        temp=temp//10
        j+=1
    div=1
    mult=1
    for i in range(1,j+1):
        if i<=k:
            div=div*10
        else:
            mult=mult*10
    q=int(n/div)
    r=int(n%div)
    rot=int(r*mult+q)
    print(n,"rotated",k,"times : ",rot)
else:
    print("Enter number in range")
