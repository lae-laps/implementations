#ifndef NEURALNET_H
#define NEURALNET_H

#include <stdlib.h>

double sigmoid(double);
double derivative_sigmoid(double);
double init_weights();

void shuffle(int *, size_t);

#endif
