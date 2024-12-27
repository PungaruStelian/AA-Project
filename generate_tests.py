import os
import random

def generate_test_file(file_index, N, T_range, element_range):
    """
    Generate a single test file pair (inX.txt and refX.txt) where no solution exists for the subset sum problem.
    """
    # Generate input data
    T = random.randint(-T_range, T_range)
    arr = [random.randint(-element_range, element_range) for _ in range(N)]

    # Write to the input file
    input_file = f"./tests/in{file_index}.txt"
    with open(input_file, "w") as infile:
        infile.write(f"{N} {T}\n")
        infile.write("\n".join(map(str, arr)) + "\n")

    # Write to the reference file
    ref_file = f"./tests/ref{file_index}.txt"
    with open(ref_file, "w") as reffile:
        reffile.write("No solution was found!\n")

# Define test cases
test_cases = [
    (100, 10000, 10000),  # Small
    (300, 100000, 100000),  # Medium
    (7000, 1000000, 1000000),  # Large
    (10000, 1000000, 1000000), # Extra Large
]

# Generate test files
os.makedirs("./tests", exist_ok=True)
for i, (N, T_range, element_range) in enumerate(test_cases, start=7):  # From in7.txt and ref7.txt
    generate_test_file(i, N, T_range, element_range)
print("Test files generated successfully.")
