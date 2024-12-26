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
    (15, 40, 40), # test 7
    (30, 60, 60), # test 8
    (45, 100, 100), # test 9
    (55, 1000, 1000), # test 10
    (65, 10000, 10000), # test 11
    (75, 100000, 100000), # test 12
    (85, 1000000, 1000000), # test 13
    (100, 1000000, 1000000), # test 14
    (110, 1000000, 1000000), # test 15
    (222, 1000000, 1000000), # test 16
    (400, 1000000, 1000000), # test 17
    (700, 1000000, 1000000), # test 18
    (1200, 1000000, 1000000), # test 19
    (2000, 1000000, 1000000), # test 20
]

# Generate test files
os.makedirs("./tests", exist_ok=True)
for i, (N, T_range, element_range) in enumerate(test_cases, start=7):  # From in7.txt and ref7.txt
    generate_test_file(i, N, T_range, element_range)
print("Test files generated successfully.")
