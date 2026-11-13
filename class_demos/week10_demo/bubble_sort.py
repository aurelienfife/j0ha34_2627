# Bubble sort algorithm in Python

# Test data 
data = [10, 21, 47, 49, 15, 40, 47, 7, 23, 13]

# Badly optimised
flag = True
cycles = 0

# Outer index: i
# Inner index: j

# Outer loop: repeat len-1 times

for i in range(len(data) - 1):
    flag = False
    # loop from second to last elements
    # But skipping the ones that are already sorted at the end
    for j in range(1, len(data) - i):
        cycles += 1
        # if current element is lower than previous
        if data[j] < data[j - 1]:
            # swap them
            data[j], data[j - 1] = data[j - 1], data[j]
            # set flag
            flag = True

    # Check: no swaps? end it all
    if not flag: break

    

print(data)
print("Cycles", cycles)