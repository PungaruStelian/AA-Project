#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "SubsetSum.h"

int ascending(const void *a, const void *b)
{
    return *(int *)a - *(int *)b;
}

int descending(const void *a, const void *b)
{
    return *(int *)b - *(int *)a;
}

bool subset_sum_backtracking(int *arr, int N, int T, int index, int *solution, int *solution_size)
{
    if (T == 0)
    {
        return true;
    }
    if (index == N)
    {
        return false;
    }

    // Includes current element
    solution[*solution_size] = index;
    (*solution_size)++;
    if (subset_sum_backtracking(arr, N, T - arr[index], index + 1, solution, solution_size))
    {
        return true;
    }
    (*solution_size)--; // Backtrack

    // Excludes current element
    return subset_sum_backtracking(arr, N, T, index + 1, solution, solution_size);
}

bool subset_sum_dp(int *arr, int N, int T, int *solution, int *solution_size)
{
    // Calculate total sum range
    long long total_sum = 0;
    for (int i = 0; i < N; i++)
    {
        if (arr[i] > 0)
            total_sum += arr[i];
        else
            total_sum -= arr[i];
    }

    // Create DP table with offset for negative numbers
    long long offset = total_sum;
    long long table_size = 2 * total_sum + 1;

    bool *dp = (bool *)malloc(table_size * sizeof(bool));
    if (dp == NULL)
    {
        printf("Eroare la alocarea memoriei pentru dp.\n");
        return false;
    }

    int *parent = (int *)malloc(table_size * sizeof(int));
    if (parent == NULL)
    {
        printf("Eroare la alocarea memoriei pentru parent.\n");
        free(dp);
        return false;
    }

    for (long long i = 0; i < table_size; i++)
    {
        parent[i] = -1;
        dp[i] = false;
    }
    dp[offset] = true; // 0 is at position offset

    // Fill the dp table
    for (int i = 0; i < N; i++)
    {
        if (arr[i] >= 0)
        {
            for (long long j = table_size - 1; j >= arr[i]; j--)
            {
                if (dp[j - arr[i]] && !dp[j])
                {
                    dp[j] = true;
                    parent[j] = i;
                }
            }
        }
        else
        {
            for (long long j = 0; j < table_size + arr[i]; j++)
            {
                if (dp[j - arr[i]] && !dp[j])
                {
                    dp[j] = true;
                    parent[j] = i;
                }
            }
        }
    }

    // Check if target sum exists
    if (!dp[T + offset])
    {
        free(dp);
        free(parent);
        return false;
    }

    // Reconstruct solution
    long long curr_sum = T + offset;
    while (curr_sum != offset)
    {
        int idx = parent[curr_sum];
        solution[*solution_size] = idx;
        (*solution_size)++;
        curr_sum -= arr[idx];
    }

    free(dp);
    free(parent);
    return true;
}

bool subset_sum_greedy(int *arr, int N, int T, int *solution, int *solution_size)
{
    typedef struct
    {
        int index;
        int value;
    } Pair;

    int compare_pairs_desc(const void *p1, const void *p2)
    {
        const Pair *a = (const Pair *)p1;
        const Pair *b = (const Pair *)p2;
        return b->value - a->value;
    }

    int compare_pairs_asc(const void *p1, const void *p2)
    {
        const Pair *a = (const Pair *)p1;
        const Pair *b = (const Pair *)p2;
        return a->value - b->value;
    }

    Pair pairs[N];
    for (int i = 0; i < N; i++)
    {
        pairs[i].index = i;
        pairs[i].value = arr[i];
    }

    if (T < 0)
        qsort(pairs, N, sizeof(Pair), compare_pairs_asc);
    else
        qsort(pairs, N, sizeof(Pair), compare_pairs_desc);

    // Greedy approach
    long long current_sum = 0;
    for (int i = 0; i < N; i++)
    {
        long long new_sum = current_sum + pairs[i].value;
        if ((new_sum <= T && pairs[i].value > 0 && T >= 0) ||
            (new_sum >= T && pairs[i].value < 0 && T < 0))
        {
            solution[*solution_size] = pairs[i].index;
            (*solution_size)++;
            current_sum = new_sum;
            // check if the sum is close enough to the target, within 10% of the target
            if (llabs(current_sum - T) <= abs(T) / 10)
                return true;
        }
    }
    return false;
}