num1 = float(input("Ente2r your first number: "))
num2 = float(input("enter your second number: "))

print("Choose an operation: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multipication")
print("4. Division")

choice= input("enter your choice(1-4): ")
if choice=="1":
    print("answer=",num1+num2)

elif choice=="2":
    print("answer=",num1-num2)

elif choice=="3":
    print("answer=",num1*num2)

elif choice=="4":
    print("answer=",num1/num2)

else:
    print("invalid choice")