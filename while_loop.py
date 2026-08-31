# While loop repeat code as long as the condition holds true. When the condition no longer holds true, we exit the while loop.
# If the code thats gets repeated inside the loop is not indented the code will result in an error.

# Loops usually include counters. A counter is a variable that keeps track of the number of iterations.

seats = 300
while seats > 0:
    print("Sell ticket")
    seats = seats - 1     # Here seats is used as a counter

# Counter variable are updated inside the loop, so they change with every iteration. An initial value is set outside the loop as the starting point.
