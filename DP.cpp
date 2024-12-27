#include <iostream>
#include <vector>
#include <algorithm>
#include "SubsetSum.h"
#include "benchmark/benchmark.h"
#include <fstream> // Added to include ifstream

/*
int main() {
    int N, T;
    std::cin >> N >> T;

    std::vector<int> arr(N);
    for (int i = 0; i < N; i++) {
        std::cin >> arr[i];
    }

    std::vector<int> solution(N);
    int solution_size = 0;

    if (subset_sum_dp(arr.data(), N, T, solution.data(), &solution_size)) {
        std::sort(solution.begin(), solution.begin() + solution_size); // Sortare implicită
        std::cout << solution_size << "\n";
        for (int i = 0; i < solution_size; i++)
            std::cout << solution[i] << " ";
        std::cout << "\n";
    } else {
        std::cout << "No solution was found!\n";
    }

    return 0;
}
*/

static void BM_DP(benchmark::State& state) {
    // Read input from a test file
    std::ifstream infile("./tests/in" + std::to_string(state.range(0)) + ".txt");
    int N, T;
    infile >> N >> T;
    std::vector<int> arr(N);
    for(int &x : arr) infile >> x;

    std::vector<int> solution(N);
    int solution_size;

    for(auto _ : state) {
        solution_size = 0; // Initialize solution_size before each call
        subset_sum_dp(arr.data(), N, T, solution.data(), &solution_size);
    }
}
BENCHMARK(BM_DP)->DenseRange(7, 20);