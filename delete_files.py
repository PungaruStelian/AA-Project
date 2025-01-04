
import os

def delete_test_files(start, end):
    for i in range(start, end + 1):
        file_path = f"./tests/in{i}.txt"
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted {file_path}")
        else:
            print(f"File not found: {file_path}")

if __name__ == "__main__":
    delete_test_files(27, 72)