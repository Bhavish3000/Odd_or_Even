"""The programe in this module calculate the given number is even or odd .
"""

number = int(input("Enter the number: "))

result = number%2

if result == 0 :
    print(f"{number} is Even Number.")

else :
    print(f"{number} is Odd number.")
