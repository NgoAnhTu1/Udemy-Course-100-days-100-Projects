num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\n--- Comparision Results ---")

if num1 == num2:
    print(f"{num1} is equal to {num2}")
if num1 > num2:
    print(f"{num1} is greater than {num2}")
if num1 < num2:
    print(f"{num1} is less than {num2}")
if num1 == 0 and num2 ==0:
    print("\nBoth numbers are zero")
elif num1 != 0 and num2 != 0:
    print("\nBoth numbers are not zero")
else:
    print("\nOne number is zero")