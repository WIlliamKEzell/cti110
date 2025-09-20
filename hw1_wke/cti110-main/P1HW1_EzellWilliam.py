# Your Name
# 2025-09-20
# Assignment: Exponent and Addition/Subtraction
# A brief description: Prompts the user for a base and exponent, computes power, then asks for three integers to add/subtract and displays results.

print("----Calculating Exponets-----\n")

# Exponent calculation
base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

print()
result = base ** exponent
print(f"{base} raised to the power of {exponent} is {result} !!!\n")

print("----Addition and Subtraction\n")

# Addition and subtraction
start = int(input("Enter a starting integer: "))
add_val = int(input("Enter a integer to add: "))
sub_val = int(input("Enter an integer to subtract: "))

print()
calc = start + add_val - sub_val
print(f"{start}+ {add_val} - {sub_val} is equal to {calc}")