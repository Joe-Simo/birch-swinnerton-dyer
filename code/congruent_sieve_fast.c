/*
 * congruent_sieve_fast.c - Ultra-Optimized Additive Scatter Sieve for Congruent Number Curves
 * Complexity: O(N^(3/2)) additive scatter sieve instead of O(N^2) search.
 * Computes exact ternary quadratic counts A32(n) and B8(n), and Tunnell coefficients
 * a(n) = A32 - B8/2 for all odd squarefree integers n up to N_MAX in parallel with OpenMP.
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <math.h>

#ifdef _OPENMP
#include <omp.h>
#endif

typedef int64_t i64;

static inline i64 isqrt_fast(i64 n) {
    if (n <= 0) return 0;
    i64 x = (i64)sqrt((double)n);
    while ((x + 1) * (x + 1) <= n) x++;
    while (x * x > n) x--;
    return x;
}

static bool *sieve_squarefree(i64 max_n) {
    bool *sqfree = (bool *)malloc((max_n + 1) * sizeof(bool));
    for (i64 i = 0; i <= max_n; i++) sqfree[i] = true;
    sqfree[0] = false;
    for (i64 p = 2; p * p <= max_n; p++) {
        i64 p2 = p * p;
        for (i64 k = p2; k <= max_n; k += p2) {
            sqfree[k] = false;
        }
    }
    return sqfree;
}

// Additive scatter sieve: O(N^(3/2)) complexity
void compute_counts_scatter(i64 max_n, int32_t *a32, int32_t *b8) {
    memset(a32, 0, (max_n + 1) * sizeof(int32_t));
    memset(b8, 0, (max_n + 1) * sizeof(int32_t));

    // Sieve A32: 2x^2 + y^2 + 32z^2 = n
    // Since n is odd, y must be odd: y = 1, 3, 5, ...
    i64 z_max_32 = isqrt_fast(max_n / 32);
    #pragma omp parallel for schedule(dynamic, 4)
    for (i64 z = 0; z <= z_max_32; z++) {
        i64 z_term = 32 * z * z;
        i64 mult_z = (z == 0) ? 1 : 2;
        i64 x_max = isqrt_fast((max_n - z_term) / 2);
        for (i64 x = 0; x <= x_max; x++) {
            i64 zx_term = z_term + 2 * x * x;
            i64 mult_zx = mult_z * ((x == 0) ? 1 : 2);
            i64 rem = max_n - zx_term;
            i64 y_max = isqrt_fast(rem);
            for (i64 y = 1; y <= y_max; y += 2) {
                i64 n = zx_term + y * y;
                #pragma omp atomic
                a32[n] += (int32_t)(mult_zx * 2);
            }
        }
    }

    // Sieve B8: 2x^2 + y^2 + 8z^2 = n
    i64 z_max_8 = isqrt_fast(max_n / 8);
    #pragma omp parallel for schedule(dynamic, 4)
    for (i64 z = 0; z <= z_max_8; z++) {
        i64 z_term = 8 * z * z;
        i64 mult_z = (z == 0) ? 1 : 2;
        i64 x_max = isqrt_fast((max_n - z_term) / 2);
        for (i64 x = 0; x <= x_max; x++) {
            i64 zx_term = z_term + 2 * x * x;
            i64 mult_zx = mult_z * ((x == 0) ? 1 : 2);
            i64 rem = max_n - zx_term;
            i64 y_max = isqrt_fast(rem);
            for (i64 y = 1; y <= y_max; y += 2) {
                i64 n = zx_term + y * y;
                #pragma omp atomic
                b8[n] += (int32_t)(mult_zx * 2);
            }
        }
    }
}

int main(int argc, char **argv) {
    i64 max_n = 511;
    bool json_output = false;
    const char *candidates_file = NULL;
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "--json") == 0) {
            json_output = true;
        } else if (strcmp(argv[i], "--export-candidates") == 0 && i + 1 < argc) {
            candidates_file = argv[++i];
        } else if (argv[i][0] != '-') {
            max_n = atoll(argv[i]);
        }
    }
    if (max_n < 1) max_n = 511;

    if (!json_output) {
        printf("=== Ultra-Fast Additive Congruent Sieve (OpenMP) ===\n");
        printf("Evaluating odd squarefree n in [1, %lld]\n", (long long)max_n);
    }

    bool *sqfree = sieve_squarefree(max_n);
    int32_t *a32 = (int32_t *)malloc((max_n + 1) * sizeof(int32_t));
    int32_t *b8 = (int32_t *)malloc((max_n + 1) * sizeof(int32_t));
    if (!a32 || !b8) {
        fprintf(stderr, "Failed to allocate memory for %lld curves\n", (long long)max_n);
        return 1;
    }

    compute_counts_scatter(max_n, a32, b8);

    FILE *cand_fp = NULL;
    if (candidates_file) {
        cand_fp = fopen(candidates_file, "w");
    }

    i64 total_tested = 0;
    i64 nonzero_a = 0;
    i64 zero_a = 0;
    i64 even_parity_order_ge_2 = 0;
    i64 odd_parity_order_ge_1 = 0;

    for (i64 n = 1; n <= max_n; n += 2) {
        if (!sqfree[n]) continue;
        total_tested++;

        i64 a_n = (i64)a32[n] - (i64)b8[n] / 2;
        if (a_n != 0) {
            nonzero_a++;
        } else {
            zero_a++;
            if ((n % 8 == 1) || (n % 8 == 3)) {
                even_parity_order_ge_2++;
                if (cand_fp) fprintf(cand_fp, "%lld\n", (long long)n);
            } else {
                odd_parity_order_ge_1++;
            }
        }
    }
    if (cand_fp) fclose(cand_fp);

    if (json_output) {
        printf("{\"max_n\": %lld, \"total_tested\": %lld, \"rank_zero_count\": %lld, \"vanishing_count\": %lld, \"even_order_ge_2\": %lld, \"odd_order_ge_1\": %lld}\n",
               (long long)max_n, (long long)total_tested, (long long)nonzero_a, (long long)zero_a, (long long)even_parity_order_ge_2, (long long)odd_parity_order_ge_1);
    } else {
        printf("\n--- Results ---\n");
        printf("Total odd squarefree n:       %lld\n", (long long)total_tested);
        printf("L(E_n, 1) != 0 (Rank 0):       %lld (%.2f%%)\n", (long long)nonzero_a, (double)nonzero_a / total_tested * 100.0);
        printf("L(E_n, 1) == 0 (Vanishing):    %lld (%.2f%%)\n", (long long)zero_a, (double)zero_a / total_tested * 100.0);
        printf("  Even order >= 2 (n=1,3 mod8): %lld\n", (long long)even_parity_order_ge_2);
        printf("  Odd order >= 1 (n=5,7 mod8):  %lld\n", (long long)odd_parity_order_ge_1);
    }

    free(sqfree);
    free(a32);
    free(b8);
    return 0;
}
