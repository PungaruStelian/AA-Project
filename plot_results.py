import csv
import matplotlib.pyplot as plt
from collections import defaultdict

def plot_times(csv_file):
    # Structura de date: { N: { 'Backtracking': timp, 'DP': timp, 'Greedy': timp } }
    data = defaultdict(dict)

    with open(csv_file, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Extract N from the first number in the test file
            test_name = row['TestFile']
            testfile = f"tests/{test_name}.txt"
            with open(testfile, 'r') as tf:
                first_line = tf.readline()
                N = int(first_line.split()[0])
            algo = row['Algorithm']
            time_s = float(row['TimeS'])
            data[N][algo] = time_s

    # Sortăm testele în ordine crescătoare după N
    tests_sorted = sorted(data.keys())
    algorithms = ['Backtracking', 'DP', 'Greedy']

    # Creează o figură mare
    plt.figure(figsize=(12, 8))

    # Pentru fiecare algoritm, colectăm timpii în ordinea testelor
    for algo in algorithms:
        times = [data[n].get(algo, 0.0) for n in tests_sorted]
        plt.plot(tests_sorted, times, marker='o', label=algo)

    # Configurăm axele și titlul
    plt.xlabel('N (number of elements)')
    plt.ylabel('Execution time (seconds)')
    plt.title('Comparison of execution times for solutions to the Subset Sum problem')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Afișăm graficul
    plt.show()

if __name__ == "__main__":
    # Apelează funcția cu "results.csv"
    plot_times('results.csv')