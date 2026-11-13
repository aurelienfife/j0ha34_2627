# Simple input validation

# Constraint integer between 0 and 50 

''' Pseudocode from Bitesize
Line 3   WHILE score ˂0 OR score ˃ 50 DO
Line 4      SEND (“The score you entered was not valid; please enter a score between 0 and 50”) TO DISPLAY
Line 5      RECEIVE score FROM (INTEGER) KEYBOARD
'''

# You need to create score
# And get a first manual
score = int(input("Enter a score between 0 and 50"))

while score < 0 or score > 50:
    print("Score is invalid. It needs to be between 0 and 50")
    score = int(input("Enter again:"))

# Another example...

password = input("What is the password?")

while password != "P@ssword123":
    print("Invalid password")
    password = input("Try again")