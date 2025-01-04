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
    (10, 50, 10),   # test 7
    (11, 50, 10),   # test 8
    (12, 100, 20),  # test 9
    (13, 200, 30),  # test 10
    (14, 200, 50),  # test 11
    (15, 300, 50),  # test 12
    (16, 300, 30),  # test 13
    (17, 400, 50),  # test 14
    (18, 400, 40),  # test 15
    (19, 200, 20),  # test 16
    (20, 100, 50),  # test 17
    (21, 100, 25),  # test 18
    (22, 120, 40),  # test 19
    (23, 150, 20),  # test 20
    (24, 100, 30),  # test 21
    (25, 100, 30),  # test 22
    (26, 100, 40),  # test 23
    (27, 100, 40),  # test 24
    (28, 120, 40),  # test 25
    (29, 120, 40),  # test 26
    (100, 100, 100),  # test 27
    (200, 200, 200),  # test 28
    (300, 300, 300),  # test 29
    (400, 400, 400),  # test 30
    (500, 500, 500),  # test 31
    (750, 750, 750),  # test 32
    (1000, 1000, 1000),  # test 33
    (1500, 1500, 1500),  # test 34
    (2000, 2000, 2000),  # test 35
    (3000, 3000, 3000),  # test 36
    (4000, 4000, 4000),  # test 37
    (5000, 5000, 5000),  # test 38
    (6000, 10000, 10000), # test 39
    (7000, 10000, 10000), # test 40
    (8000, 10000, 10000), # test 41
    (9000, 10000, 10000), # test 42
    (10100, 10000, 10000), # test 43
    (10200, 100000, 100000), # test 44
    (10300, 100000, 100000), # test 45
    (10400, 100000, 100000), # test 46
    (10500, 100000, 100000), # test 47
    (10600, 100000, 100000), # test 48
    (10700, 1000000, 1000000), # test 49
    (10800, 1000000, 1000000), # test 50
    (10900, 1000000, 1000000), # test 51
    (11000, 1000000, 1000000), # test 52
    (11100, 1000000, 1000000), # test 53
]

# Generate test files
os.makedirs("./tests", exist_ok=True)
for i, (N, T_range, element_range) in enumerate(test_cases, start=7):  # From in7.txt and ref7.txt
    generate_test_file(i, N, T_range, element_range)
print("Test files generated successfully.")