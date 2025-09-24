def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b!=0:
        return a/b
    else:
        print("Error : Division By Zero")

while True:
    print("\n===Simple Calculator===\n")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Quit")
    
        
    choice=input("Enter the choice(1/2/3/4 or q): ")
    a=float(input("Enter the first number  :"))
    b=float(input("Enter the second number  :"))

    if choice == '1':
        print("Result :",add(a,b))
    elif choice == '2':
        print("Result :",sub(a,b))
    elif choice == '3':
        print("Result :",multiply(a,b))
    elif choice == '4':
        print("Result :",divide(a,b))
    elif choice == 'q':
        print("Quit")
        break
    else:
        print("Invalid choice, please enter 1-5")
    
    restart = input("\nDo you want to perform another operations? (yes/no): ")
    if restart == "no":
        print("Thank you for using Calculator")
        break
