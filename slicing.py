# Slicing allow you to extract a portion of a list
# Starting & Stopping indexes are separated by a colon

animals = ["cat","dog","bird","cow"]
print(animals[1:3])   # O/P is ['dog', 'bird']

'''
        animals = ["cat","dog","bird","cow"]
        
                    cat   dog   bird   cow
                   0    1     2      3     4
'''

# Slicing also works on string

vehicle = "airplane"
print(vehicle[0:3])  # O/P is air

# Slicing a list will produce another list
# Slicing a string will produce another string

# When slicing you can omit the starting index. This means that you'll be slicing from the very first element.

cart = ["lamp","candles","chair","carpet"]
print(cart[:3])  # O/P is ['lamp', 'candles', 'chair']

vehicle = 'motorbike'
print(vehicle[:5])   # O/P is motor

# When slicing you can omit the stopping index. This means that you'll be slicing until the very last element

cart = ["lamp","candles","chair","carpet"]
print(cart[1:])   # O/P is ['candles', 'chair', 'carpet']



# Python support indexing from the end called negative indexing. This means the last value of a sequence has an index of -1
'''
animals = ["cat","dog","bird","cow"]
                    cat   dog   bird   cow
                   -4   -3    -2     -1
'''

animals = ["cat","dog","bird","cow"]
print(animals[-1])      # O/P is cow
print(animals[-2])      # O/P is bird
print(animals[-3:])     # O/P is ['dog', 'bird', 'cow']
print(animals[-3:-1])   # O/P is ['dog', 'bird']

# We can combine positive with negative indexing when slicing

C = ['$','%','&','*']
print(C[1:-1])   # O/P is ['%', '&']

C = ['$','%','&','*']
C[:2] = ['A','B']
print(C)   # O/P is ['A', 'B', '&', '*']