# Initial list
numbers = [3, 1, 4, 1, 5, 9, 2]

# The following are the expected values for each expression


# numbers[0] should be 3 (first element)
# numbers[-1] should be 2 (last element)
# numbers[3] should be 1 (index 3 is the fourth element)
# numbers[:-1] should be [3, 1, 4, 1, 5, 9] (all elements except the last one)
# numbers[3:4] should be [1] (a slice of the element at index 3, inclusive of 3 and exclusive of 4)
# 5 in numbers should be True (5 is an element of the list)
# 7 in numbers should be False (7 is not in the list)
# "3" in numbers should be False ("3" is a string, not an integer)
# numbers + [6, 5, 3] should be [3, 1, 4, 1, 5, 9, 2, 6, 5, 3] (concatenating two lists)

# test the expressions:
print(numbers[0])  # Expected: 3
print(numbers[-1])  # Expected: 2
print(numbers[3])  # Expected: 1
print(numbers[:-1])  # Expected: [3, 1, 4, 1, 5, 9]
print(numbers[3:4])  # Expected: [1]
print(5 in numbers)  # Expected: True
print(7 in numbers)  # Expected: False
print("3" in numbers)  # Expected: False
print(numbers + [6, 5, 3])  # Expected: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Modify the list
numbers[0] = "ten"
numbers[-1] = 1  

# Print the modified list
print(numbers[2:])  # Expected output should be the list excluding the first two elements

# Check if 9 is in the modified list
print(9 in numbers)  # Expected output: True (since 9 is still in the list)
