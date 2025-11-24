a=int(input("enter a number:"))
b=int(input("enter a another number:"))
print("1.add")
print("2.subtract")
print("3.multiplication")
print("4.division")
choice=int(input("choose 1-4"))
if choice==1:
    print("result",a+b)
elif choice ==2:
    print("result",a-b)
elif choice ==3:
    print("result",a*b)
elif choice ==4:
    print("result",a/b)
else:
    print("invalid choice")