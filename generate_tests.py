#!/usr/bin/env python3
import os
import random

def generate_test_file(file_index, N, T_range, element_range):
    """
    Generate a single test file pair (inX.txt and refX.txt) where no solution exists for the subset sum problem.
    """
    # Generate input data
    arr = [random.randint(-element_range, element_range) for _ in range(N)]
    
    # Calculate the sum of all positive numbers and all negative numbers
    positive_sum = sum(x for x in arr if x > 0)
    negative_sum = sum(x for x in arr if x < 0)
    
    # Set T to be greater than positive_sum or less than negative_sum to ensure no subset sums to T
    if random.choice([True, False]):
        # Set T greater than the total positive sum
        T = positive_sum + random.randint(1, element_range)
    else:
        # Set T less than the total negative sum
        T = negative_sum - random.randint(1, element_range)
    
    # Ensure T is within the specified range
    T = max(-T_range, min(T, T_range))
    
    # Write to the input file
    input_file = f"./tests/in{file_index}.txt"
    with open(input_file, "w") as infile:
        infile.write(f"{N} {T}\n")
        infile.write("\n".join(map(str, arr)) + "\n")
    
# Define test cases
test_cases = [
    (20, 200, 2), # test 7
    (20, 2, 200), # test 8
    (20, 1000000, 50000), # test 9
    (20, 50000, 1000000), # test 10
    (30, 30, 3000), # test 11
    (30, 30, 300), # test 12
    (30, 3000, 30), # test 13
    (30, 300, 30), # test 14
    (30, 30, 30), # test 15
    (40, 40, 4000), # test 16
    (40, 40, 400), # test 17
    (40, 4000, 40), # test 18
    (40, 400, 40), # test 19
    (40, 40, 40), # test 20
]

# Generate test files
os.makedirs("./tests", exist_ok=True)
for i, (N, T_range, element_range) in enumerate(test_cases, start=7):  # From in7.txt and ref7.txt
    generate_test_file(i, N, T_range, element_range)
print("Test files generated successfully.")