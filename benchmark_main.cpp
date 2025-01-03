#include "benchmark/benchmark.h"
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <functional>
#include <fstream>

#ifdef _WIN32
    #include <windows.h>
    #include <psapi.h>
    static double getPeakMemoryMB() {
        PROCESS_MEMORY_COUNTERS_EX pmc;
        GetProcessMemoryInfo(GetCurrentProcess(), (PROCESS_MEMORY_COUNTERS*)&pmc, sizeof(pmc));
        return (pmc.PeakWorkingSetSize) / (1024.0 * 1024.0);
    }
    static void resetPeakMemory() {
        SetProcessWorkingSetSizeEx(GetCurrentProcess(), -1, -1, 0);
        EmptyWorkingSet(GetCurrentProcess());
    }
#else
    #include <sys/resource.h>
    #include <malloc.h>
    static double getPeakMemoryMB() {
        struct rusage usage;
        getrusage(RUSAGE_SELF, &usage);
        return usage.ru_maxrss / 1024.0;
    }
    static void resetPeakMemory() {
        malloc_trim(0);
    }
#endif

static double measurePeakMemory(const std::function<void()>& f) {
    resetPeakMemory();
    double before = getPeakMemoryMB();
    f();
    double after = getPeakMemoryMB();
    resetPeakMemory();
    return std::abs(after - before);
}

namespace benchmark {
    struct State;
    benchmark::State* current_state = nullptr;  // Definition
}

class CustomMemoryReporter : public benchmark::ConsoleReporter {
private:
    std::ofstream csv_file;

public:
    CustomMemoryReporter() : csv_file("benchmark_results.csv") {
        if (csv_file.is_open()) {
            csv_file << "Benchmark,Time(ms),Memory(MB)\n";
        }
    }

    ~CustomMemoryReporter() {
        if (csv_file.is_open()) {
            csv_file.close();
        }
    }

    bool ReportContext(const Context& context) override {
        // Keep existing console output
        std::cout << std::left << std::setw(20) << "Benchmark"
                  << std::right << std::setw(20) << "Time(ms)"
                  << std::right << std::setw(20) << "Memory(MB)"
                  << "\n------------------------------------------------------------\n";
        return true;
    }

    void ReportRuns(const std::vector<Run>& reports) override {
        if (reports.empty()) return;
        
        for (auto& r : reports) {
            double real_per_iter_ms = r.real_accumulated_time * 1e3 / r.iterations;
            double mem_usage_mb = 0.0;
            if (r.counters.find("MemMB") != r.counters.end()) {
                mem_usage_mb = r.counters.at("MemMB");
            }

            // Console output (keep existing format)
            std::cout << std::left << std::setw(20) << r.benchmark_name()
                      << std::right << std::setw(20) << real_per_iter_ms
                      << std::right << std::setw(20) << mem_usage_mb
                      << "\n";

            // CSV output
            if (csv_file.is_open()) {
                csv_file << r.benchmark_name() << ","
                        << real_per_iter_ms << ","
                        << mem_usage_mb << "\n";
            }
        }
    }
};

int main(int argc, char** argv) {
    benchmark::Initialize(&argc, argv);
    CustomMemoryReporter reporter;
    benchmark::RunSpecifiedBenchmarks(&reporter);
    benchmark::Shutdown();
    return 0;
}