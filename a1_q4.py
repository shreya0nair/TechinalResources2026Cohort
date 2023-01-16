low=int(input("Enter lower limit of range : "))
high=int(input("Enter higher limit of range : "))
print("Prime numbers between",low ,"and",high,"are :")
for i in range(low,high+1):
    if (2<=low<high<(10**6)):
        for n in range(2,i):
            if (i%n)==0:
                break
        else:
            print(i)
