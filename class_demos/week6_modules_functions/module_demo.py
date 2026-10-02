# Import whole module
import datetime

# Selectively import part of one module
from random import randint

# module.class.function
ts1 = datetime.datetime.now()    
name = input("What is your name?")   # Built-in function
ts2 = datetime.datetime.now()
diff = ts2 - ts1

# We imported randint directly, no need to chain the module
# Function from built-in module (randint)
print("Here is a random number:", randint(1,100))  
input()

print("It took you", diff, "seconds to respond")