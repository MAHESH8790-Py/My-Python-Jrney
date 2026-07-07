import math
print("Simple Calculator")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\n1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6.Power")
print("7.square root")
print("8.cube root")
print("9.Floor division")

choice = input("Enter your choice (1-5): ")

if choice == "1":
    print("Answer =", a + b)

elif choice == "2":
    print("Answer =", a - b)

elif choice == "3":
    print("Answer =", a * b)

elif choice == "4":
    if b != 0:
        print("Answer =", a / b)
    else:
        print("Cannot divide by zero!")

elif choice == "5":
       print("Answer =", a % b)
elif choice=="6":
       print("Answer=",a**b)
elif choice=="7":
       print("square root of first number =",math.sqrt(a))
elif choice=="8":
       print("Answer=",a**3)
elif choice=="9":
       print("Answer=",a//b)
elif choice=="10":
       pribt("Thank you for using calculator")
     
 

else:
    print("Invalid choice")