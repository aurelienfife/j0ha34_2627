# Function 'signature'
# Includes parameters
def times_table(number, limit=10):  # Add 'parameters' (aka formal parameters)
    # For 1 to limit
    for i in range(limit):
        print(f"{i+1} x {number} = {(i+1)*number}")

# Function has a 'scope' 


def main():
    num = int(input("Enter a positive integer:"))
    # num is an 'argument'
    times_table(num)  # This will actually call the function

    print()

    times_table(num, 20)


# Checks that the module loaded is the "main" program
# And then calls the main() function
if __name__ == "__main__":
    main()
