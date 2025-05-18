numer1 = float(input("Enter the first number: "))
numer2 = float(input("Enter the second number: "))

addition = numer1 + numer2
subtraction = numer1 - numer2
multiplication = numer1 * numer2
division = numer1 / numer2 if numer2 != 0 else "Cannot divide by zero"

print("\n--- Calculator Results ---")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)