n=int(input("Enter a number : "))
for i in range(1,n//2+2):
    for j in range(1,i+1):
        print("    *",end='')
    print()
for k in range(1,n//2+1):
    for l in range(0,n//2-k+1):
        if k==1:
            print("    *",end='')
        else:
            print("    *",end='')
    print()
  
