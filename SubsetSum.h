#ifndef SUBSETSUM_H
#define SUBSETSUM_H

#include <stdbool.h>
#include "benchmark/benchmark.h"

// Declare namespace and extern variable before extern "C"
namespace benchmark {
    extern benchmark::State* current_state;
}

#ifdef __cplusplus
extern "C" {
#endif

/**
 * Compare function for ascending order.
 */
int ascending(const void *a, const void *b);

/**
 * Compare function for descending order.
 */
int descending(const void *a, const void *b);

/**
 * Average time complexity: O(2^N).
 * Space: O(N) (due to recursion stack).
 */
bool subset_sum_backtracking(int *arr, int n, int T, int index, int *solution, int *solution_size);

/**
 * Approximate the sum of all elements with N * T
 * Average time complexity: O(T * N^2).
 * Space: O(T * N).
 */
bool subset_sum_dp(int *arr, int n, int T, int *solution, int *solution_size);

/**
 * Average time complexity: O(N * log(N)).
 * Space: O(N).
 */
bool subset_sum_greedy(int *arr, int n, int T, int *solution, int *solution_size);

#ifdef __cplusplus
}
#endif

#endif // SUBSETSUM_H