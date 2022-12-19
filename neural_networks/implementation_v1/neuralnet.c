#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#include "neuralnet.h"

double sigmoid(double x) {
    return 1 / (1 + exp(-x));
}

double derivative_sigmoid(double x) {
    return x * (1 - x);
}

double init_weights() { 
    return ((double)rand()) / ((double)RAND_MAX); 
}

// shuffle randomly an array of data
void shuffle(int *array, size_t n) {
    if (n > 1) {
        size_t i;
        for (i = 0; i < n - 1; i++) {
            size_t j = i + rand() / (RAND_MAX / (n - i) + 1); 
            int t = array[j];
            array[j] = array[i];
            array[i] = t;
        }
    }
}

