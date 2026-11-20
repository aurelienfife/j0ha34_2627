import array   # makes single-type array available

# Bubble sort - typical implementation in Python
data = array.array('i', [10,5,7,23,68,44])     # Creating an empty array
                            # of signed ints ('i')

# The array above can substituted with a normal Python 'list'
# but it's best to have a single type of data for a sort 
# algorithm, because Python crash behave when comparing different types

# Bubble sort function
def bubble_sort(unsorted_data): # Argument: a list or array
    # Outer loop keeps track of runs
    # Allows to reduce length of inner loop
    # Because last elements will be sorted
    for i in range(len(data)):
        flag = False
        # Inner loop looks for elements out of 
        # place and swaps them
        for j in range(1, len(data)-i):
            # If data out of place, swap them
            if data[j] < data[j-1]:
                # in Python a,b=b,a swaps a and b
                # Other languages don't necessarily implement 
                # this shortcut
                data[j], data[j-1] = data[j-1], data[j]

                # e.g. in c++, javascript etc 
                # you would do something like
                # c=a
                # a=b
                # b=c

                # if swap happened: raise flag
                flag = True

        # if no swaps, exit loop
        if flag is False:
            return

# Test code
print(data)
bubble_sort(data)
print(data)

