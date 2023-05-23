#include <math.h>
#include <stdio.h>

#define increment 0.1

double calculate_base_constant(double base) {
    double base_cte = (pow(base, increment) / increment);
    return base_cte;
}

int main() {
    double base = 0;
    for (int i = 0; i < 100; i++) {
        double base_cte = calculate_base_constant(base);
        printf("base: %.2g ; cte: %g\n", base, base_cte);
        base += 0.1; 
    }

    return 0;
}

