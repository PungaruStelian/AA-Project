import csv
import matplotlib.pyplot as plt
from collections import defaultdict

def get_N_from_file(test_number):
    try:
        with open(f"./tests/in{test_number}.txt", 'r') as f:
            N = int(f.readline().split()[0])
            return N
    except Exception as e:
        print(f"Error reading N from test file {test_number}: {e}")
        return None

def plot_metrics(csv_file):
    try:
        print(f"Trying to open {csv_file}...")
        data = defaultdict(lambda: defaultdict(dict))
        
        with open(csv_file, 'r', newline='') as f:
            reader = csv.DictReader(f)
            print("\nCSV Headers:", reader.fieldnames)
            
            for row in reader:
                print(f"\nProcessing row: {row}")
                benchmark = row['Benchmark'].strip()
                if '/' in benchmark:
                    algo, test_num = benchmark.split('/')
                    algo = algo[3:]  # Remove "BM_" prefix
                    test_num = int(test_num)
                    
                    # Get actual N from test file
                    N = get_N_from_file(test_num)
                    if N is None:
                        continue

                    time_ms = float(row['Time(ms)'])
                    memory_mb = float(row['Memory(MB)'])
                    
                    data[N][algo] = {
                        'time': time_ms / 1000,  # Convert to seconds
                        'memory': memory_mb
                    }
                    print(f"Added data point: N={N}, algo={algo}, time={time_ms}ms, memory={memory_mb}MB")

        if not data:
            print("No data was loaded!")
            return

        # Sort by N values
        N_values = sorted(data.keys())
        print(f"\nFound N values: {N_values}")
        
        algorithms = ['Backtracking', 'DP', 'Greedy']
        colors = ['red', 'blue', 'green']
        markers = ['o', 's', '^']
        
        # Create time plot
        plt.figure(figsize=(12, 6))
        for algo, color, marker in zip(algorithms, colors, markers):
            times = []
            ns = []
            for n in N_values:
                if algo in data[n] and data[n][algo]['time'] is not None:
                    ns.append(n)
                    times.append(data[n][algo]['time'])
            if times:
                plt.plot(ns, times, marker=marker, label=algo, color=color, linewidth=2, markersize=8)
        
        plt.xlabel('N (number of elements)', fontsize=12)
        plt.ylabel('Execution time (seconds)', fontsize=12)
        plt.title('Execution Time Comparison', fontsize=14)
        plt.legend(fontsize=10)
        plt.grid(True)
        plt.yscale('log')
        plt.tight_layout()
        plt.savefig('time_comparison.png', dpi=300, bbox_inches='tight')
        print("\nSaved time plot to time_comparison.png")
        plt.close()

        # Create memory plot
        plt.figure(figsize=(12, 6))
        for algo, color, marker in zip(algorithms, colors, markers):
            memory = []
            ns = []
            for n in N_values:
                if algo in data[n] and data[n][algo]['memory'] is not None:
                    ns.append(n)
                    memory.append(data[n][algo]['memory'])
            if memory:
                plt.plot(ns, memory, marker=marker, label=algo, color=color, linewidth=2, markersize=8)
        
        plt.xlabel('N (number of elements)', fontsize=12)
        plt.ylabel('Memory usage (MB)', fontsize=12)
        plt.title('Memory Usage Comparison', fontsize=14)
        plt.legend(fontsize=10)
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('memory_comparison.png', dpi=300, bbox_inches='tight')
        print("Saved memory plot to memory_comparison.png")
        plt.close()

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    plot_metrics('benchmark_results.csv')