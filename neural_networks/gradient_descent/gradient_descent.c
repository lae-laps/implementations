#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#define epochs 50
#define stepsize 0.1

double polinomial(double x) {
    // f(x) = x^2 + 3x - 4
    // f'(x) = 2x + 3 

    return x * x + 3.0 * x - 4.0;
}

double derivative(double x) {
    return abs(2.0 * x + 3.0);
}

int main() {
    // starting point -> (2,6)
    
    double x = 2.0;
    double y = polinomial(x);

    //for (int i = 0; i < epochs; i++) {
    for (;;) {
        double gradient = derivative(x);
        printf("(%g, %g) | tg: %g\n", x, y, gradient);

        if (gradient <= 0.2 && gradient >= -0.2) {
            printf(" * Found local Minimum -> (%g, %g)\n", x, y);
            exit(0);
        } else {
            x -= stepsize;
        }
    }

    return 0;
}

