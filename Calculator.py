def addition():
    n1=int(input("Enter the first number: "))
    n2=int(input("Enter the second number: "))
    add=n1+n2
    print("Addition of {} and {} is {}".format(n1,n2,add))
    
def subtraction():
    n1=int(input("Enter the first number: "))
    n2=int(input("Enter the second number: "))
    sub=n1-n2
    print("subtraction of {} and {} is {}".format(n1,n2,sub))
    
def multiplication():
    n1=int(input("Enter the first number: "))
    n2=int(input("Enter the second number: "))
    mul=n1*n2
    print("multiplication of {} and {} is {}".format(n1,n2,mul))
    
def division():
    n1=int(input("Enter the first number: "))
    n2=int(input("Enter the second number: "))
    div=n1/n2
    print("division of {} and {} is {}".format(n1,n2,div))

while True:
    print("choose operator\n1.+\n2.-\n3.*\n4./\n5.Exit")
    choice=int(input("Enter choice: "))
    if choice==1:
        addition()
    elif choice==2:
        subtraction()
    elif choice==3:
        multiplication()
    elif choice==4:
        division()
    elif choice==5:
        break
    else:
        print("Invalid options")
