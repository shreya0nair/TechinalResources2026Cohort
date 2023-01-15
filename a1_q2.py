marks=int(input("Enter marks of the student : "))
if marks<0 or marks>100:
    print("Invalid entry")
elif marks>90:
    print("Excellent")
elif 80<marks<=90:
    print("Good")
elif 70<marks<=80:
    print("Fair")
elif 60<marks<=70:
    print("Meets expectations")
elif marks<=60:
    print("Below par")
