# Conditional or if-else statement allow programs to perform different action based on the conditions

age = 16
if age > 18:
    print("Regular price")
else:
    print("Discount")

# You can use the elif statement to check for more conditions if the first condition is not met

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Fail")