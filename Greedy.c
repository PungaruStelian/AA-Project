#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "SubsetSum.c"

int main() {
    int N, T;
    scanf("%d %d", &N, &T);

    int arr[N];
    for (int i = 0; i < N; i++) {
        scanf("%d", &arr[i]);
    }

    int solution[N];
    int solution_size = 0;

    if (subset_sum_greedy(arr, N, T, solution, &solution_size))
    {
        qsort(solution, solution_size, sizeof(int), ascending);
        printf("%d\n", solution_size);
        for (int i = 0; i < solution_size; i++)
            printf("%d ", solution[i]);
        printf("\n");
    } else
        printf("No solution was found!\n");

    return 0;
}