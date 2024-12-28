#include <iostream>
#include <vector>
#include <algorithm>
#include "SubsetSum.h"
#include "benchmark/benchmark.h"
#include <fstream> // Added to include ifstream
#include <functional>

#ifdef _WIN32
#include <windows.h>
#include <psapi.h>
static double getMemoryMB() {
    PROCESS_MEMORY_COUNTERS pmc;
    GetProcessMemoryInfo(GetCurrentProcess(), &pmc, sizeof(pmc));
    return pmc.WorkingSetSize / (1024.0 * 1024.0);
}
#else
#include <unistd.h>
#include <fstream>
#include <malloc.h>
static double getMemoryMB() {
    std::ifstream infile("/proc/self/statm");
    if (!infile) return 0.0;
    long pages;
    infile >> pages;
    long pageSize = sysconf(_SC_PAGE_SIZE);
    return (pages * pageSize) / (1024.0 * 1024.0);
}
#endif

static double measureMemoryDiff(const std::function<void()>& f) {
    double before = getMemoryMB();
    f(); // run your test code
#ifdef __linux__
    malloc_trim(0);
#endif
#ifdef _WIN32
    HANDLE hProcess = GetCurrentProcess();
    SetProcessWorkingSetSize(hProcess, (SIZE_T)-1, (SIZE_T)-1);
#endif
    double after = getMemoryMB();
    // Report the positive difference
    return (after > before) ? (after - before) : 0.0;
}

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
        benchmark::current_state = &state;
        solution_size = 0;
        subset_sum_dp(arr.data(), N, T, solution.data(), &solution_size);
        benchmark::current_state = nullptr;
    }
}
BENCHMARK(BM_DP)->DenseRange(7, 20);