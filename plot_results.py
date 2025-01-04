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
                    
                    # Modify the data mapping to use test_num instead of N
                    data[test_num][algo] = {
                        'N': N,
                        'time': time_ms / 1000,  # Convert to seconds
                        'memory': memory_mb
                    }
                    print(f"Added data point: Test={test_num}, algo={algo}, N={N}, time={time_ms}ms, memory={memory_mb}MB")

        if not data:
            print("No data was loaded!")
            return

        # Define test ranges based on test numbers
        ranges = {
            'Trio': range(7, 27),
            'Duo': range(27, 35),
            'Solo': range(35, 54)
        }

        # Define which algorithms to include per range
        algo_inclusion = {
            'Trio': ['Backtracking', 'DP', 'Greedy'],
            'Duo': ['DP', 'Greedy'],
            'Solo': ['Greedy']
        }

        # Define colors and markers
        colors = {'Backtracking': 'red', 'DP': 'blue', 'Greedy': 'green'}
        markers = {'Backtracking': 'o', 'DP': 's', 'Greedy': '^'}

        for range_name, test_range in ranges.items():
            # Collect data for current range based on test_num
            current_data = defaultdict(dict)
            for test_num in test_range:
                if test_num in data:
                    for algo in algo_inclusion[range_name]:
                        if algo in data[test_num]:
                            current_data[test_num][algo] = data[test_num][algo]
            
            if not current_data:
                print(f"No data available for {range_name}. Skipping plots.")
                continue

            # Prepare lists for plotting
            plot_algos = algo_inclusion[range_name]
            plot_colors = [colors[algo] for algo in plot_algos]
            plot_markers = [markers[algo] for algo in plot_algos]

            # Create Execution Time Comparison Plot
            plt.figure(figsize=(12, 6))
            for algo, color, marker in zip(plot_algos, plot_colors, plot_markers):
                ns = []
                times = []
                for test_num in sorted(current_data.keys()):
                    if algo in current_data[test_num]:
                        ns.append(current_data[test_num][algo]['N'])
                        times.append(current_data[test_num][algo]['time'])
                if times:
                    plt.plot(ns, times, marker=marker, label=algo, color=color, linewidth=2, markersize=8)
            plt.xlabel('N (number of elements)', fontsize=12)
            plt.ylabel('Execution Time (seconds)', fontsize=12)
            plt.title(f'Execution Time Comparison: {range_name}', fontsize=14)
            plt.legend(fontsize=10)
            plt.grid(True)
            plt.yscale('log')
            plt.tight_layout()
            plt.savefig(f'{range_name.lower()}_time_comparison.png', dpi=300, bbox_inches='tight')
            print(f"Saved execution time plot to {range_name.lower()}_time_comparison.png")
            plt.close()

            # Create Memory Usage Comparison Plot
            plt.figure(figsize=(12, 6))
            for algo, color, marker in zip(plot_algos, plot_colors, plot_markers):
                ns = []
                memories = []
                for test_num in sorted(current_data.keys()):
                    if algo in current_data[test_num]:
                        ns.append(current_data[test_num][algo]['N'])
                        memories.append(current_data[test_num][algo]['memory'])
                if memories:
                    plt.plot(ns, memories, marker=marker, label=algo, color=color, linewidth=2, markersize=8)
            plt.xlabel('N (number of elements)', fontsize=12)
            plt.ylabel('Memory Usage (MB)', fontsize=12)
            plt.title(f'Memory Usage Comparison: {range_name}', fontsize=14)
            plt.legend(fontsize=10)
            plt.grid(True)
            plt.tight_layout()
            plt.savefig(f'{range_name.lower()}_memory_comparison.png', dpi=300, bbox_inches='tight')
            print(f"Saved memory usage plot to {range_name.lower()}_memory_comparison.png")
            plt.close()

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    plot_metrics('benchmark_results.csv')