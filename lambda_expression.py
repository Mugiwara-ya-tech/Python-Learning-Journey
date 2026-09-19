# Lambda expression are function without a name that are quick to create & use. They are written in just one line using the lambda keyword and are often used for small, simple tasks.
greet = lambda name: "Welcome," + name
print(greet("Bob"))     # O/P is Welcome,Bob

# Lambda expression are called anonymous function. This mean that they dont need a name while being defined

# lambda <arguments> : <expression>

# lambda expression perform a single operation and return a result. They are define using the lambda keyword, followed by it argument, a colon and the expression to perform

# You can assign the lambda expression to a variable and then call its a regular function
discount = lambda price: price * 0.9
print(discount(100))     # O/P is 90.0

# Lambda expression can take multiple argument separated by commas
lambda width, height : width * height

# You can provide argument to lambda expression on-the-fly by adding them in parenthesis immediately after the lambda function. The lambda expression should also be enclosed in parentheses
res = (lambda x,y: x+y)(2,3)
print(res)     # O/P is 5