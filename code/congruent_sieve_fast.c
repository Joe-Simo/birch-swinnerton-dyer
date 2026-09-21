/*
 * congruent_sieve_fast.c - Hardware-accelerated ternary quadratic form sieve
 * Computes A32(n) and B8(n) counts and Tunnell coefficients a(n) = A32 - B8/2
 * for odd squarefree integers n up to N_MAX in parallel with OpenMP.
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

// Fast integer square root
static inline i64 isqrt_fast(i64 n) {
    if (n <= 0) return 0;
    i64 x = (i64)sqrt((double)n);
    while ((x + 1) * (x + 1) <= n) x++;
    while (x * x > n) x--;
    return x;
}

// Check squarefree via precomputed sieve
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

// Compute ternary count: sum over signed triples 2x^2 + y^2 + coeff_z * z^2 = n
i64 count_ternary(i64 n, i64 coeff_z) {
    i64 total = 0;
    i64 z_max = isqrt_fast(n / coeff_z);
    for (i64 z = 0; z <= z_max; z++) {
        i64 rem_z = n - coeff_z * z * z;
        i64 x_max = isqrt_fast(rem_z / 2);
        for (i64 x = 0; x <= x_max; x++) {
            i64 rem_y = rem_z - 2 * x * x;
            i64 y = isqrt_fast(rem_y);
            if (y * y == rem_y) {
                i64 mult_x = (x == 0) ? 1 : 2;
                i64 mult_y = (y == 0) ? 1 : 2;
                i64 mult_z = (z == 0) ? 1 : 2;
                total += mult_x * mult_y * mult_z;
            }
        }
    }
    return total;
}

int main(int argc, char **argv) {
    i64 max_n = 511;
    if (argc > 1) {
        max_n = atoll(argv[1]);
    }
    if (max_n < 1) max_n = 511;

    bool json_output = false;
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "--json") == 0) json_output = true;
    }

    if (!json_output) {
        printf("=== Congruent Sieve Fast (OpenMP) ===\n");
        printf("Evaluating odd squarefree n in [1, %lld]\n", (long long)max_n);
    }

    bool *sqfree = sieve_squarefree(max_n);

    i64 total_tested = 0;
    i64 nonzero_a = 0;
    i64 zero_a = 0;
    i64 even_parity_order_ge_2 = 0;
    i64 odd_parity_order_ge_1 = 0;

    #pragma omp parallel for reduction(+:total_tested, nonzero_a, zero_a, even_parity_order_ge_2, odd_parity_order_ge_1) schedule(dynamic, 64)
    for (i64 n = 1; n <= max_n; n += 2) {
        if (!sqfree[n]) continue;
        total_tested++;

        i64 a32 = count_ternary(n, 32);
        i64 b8  = count_ternary(n, 8);
        i64 a_n = a32 - b8 / 2;

        if (a_n != 0) {
            nonzero_a++;
        } else {
            zero_a++;
            if ((n % 8 == 1) || (n % 8 == 3)) {
                even_parity_order_ge_2++;
            } else {
                odd_parity_order_ge_1++;
            }
        }
    }

    if (json_output) {
        printf("{\"max_n\": %lld, \"total_tested\": %lld, \"rank_zero_count\": %lld, \"vanishing_count\": %lld, \"even_order_ge_2\": %lld, \"odd_order_ge_1\": %lld}\n",
               (long long)max_n, (long long)total_tested, (long long)nonzero_a, (long long)zero_a, (long long)even_parity_order_ge_2, (long long)odd_parity_order_ge_1);
    } else {
        printf("\n--- Results ---\n");
        printf("Total odd squarefree n:       %lld\n", (long long)total_tested);
        printf("L(E_n, 1) != 0 (Rank 0):       %lld\n", (long long)nonzero_a);
        printf("L(E_n, 1) == 0 (Vanishing):    %lld\n", (long long)zero_a);
        printf("  Even order >= 2 (n=1,3 mod8): %lld\n", (long long)even_parity_order_ge_2);
        printf("  Odd order >= 1 (n=5,7 mod8):  %lld\n", (long long)odd_parity_order_ge_1);
    }

    free(sqfree);
    return 0;
}
