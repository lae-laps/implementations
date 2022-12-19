// Simple neural network to learn the XOR function

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#include "neuralnet.h"

#define numInput 2
#define numHiddenNodes 2        // try setting a higher value
#define numOutputs 1
#define numTrainingSets 4

int main() {
   
    double error_progression[100000];

    const double learning_rate = 1.0f;
    
    double hiddenLayer[numHiddenNodes];
    double outputLayer[numOutputs];

    double hiddenLayerBias[numHiddenNodes];
    double outputBias[numOutputs];

    double hiddenWeights[numInput][numHiddenNodes];
    double outputWeights[numHiddenNodes][numOutputs];

    // training data
    
    double training_inputs[numTrainingSets][numInput] = {
        {0.0f, 0.0f},
        {1.0f, 0.0f},
        {0.0f, 1.0f},
        {1.0f, 1.0f},
    };
    
    double training_outputs[numTrainingSets][numOutputs] = {
        {0.0f},
        {1.0f},
        {1.0f},
        {0.0f},
    };
    

    for (int i = 0; i < numInput; i++) {
        for (int j = 0; j < numHiddenNodes; j++) {
            hiddenWeights[i][j] = init_weights(); 
        } 
    }

    for (int i = 0; i < numHiddenNodes; i++) {
        for (int j = 0; j < numOutputs; j++) {
            outputWeights[i][j] = init_weights(); 
        } 
    }

    for (int i = 0; i < numOutputs; i++) {
        outputBias[i] = init_weights();
    }

    int trainingSetOrder[] = {0, 1, 2, 3};
    int numberOfEpochs = 100000;

    // Training
    
    for (int epoch = 0; epoch < numberOfEpochs; epoch++) {
        shuffle(trainingSetOrder, numTrainingSets);
        
        for (int x = 0 ; x < numTrainingSets; x++) {
            int i = trainingSetOrder[x];
                
            // Forward pass in neural network   
            // Compute hidden layer activation
            for (int j = 0; j < numHiddenNodes; j++) {
                double activation = hiddenLayerBias[j];
                for (int k = 0; k < numInput; k++) {
                    activation += training_inputs[i][k] * hiddenWeights[k][j];
                }
                hiddenLayer[j] = sigmoid(activation);
            }
                
            // Compute output layer activation
            for (int j = 0; j < numOutputs; j++) {
                double activation = outputBias[j];
                for (int k = 0; k < numHiddenNodes; k++) {
                    activation += hiddenLayer[k] * outputWeights[k][j];
                }
                outputLayer[j] = sigmoid(activation);
            }
                
            printf("input: <%g> <%g>  / output: %g / expected: %g / error -> %g \n", training_inputs[i][0], training_inputs[i][1], outputLayer[0], training_outputs[i][0], (outputLayer[0] - training_outputs[i][0]));
            //printf("%g, ", (outputLayer[0] - training_outputs[i][0]));
            error_progression[i] = outputLayer[0] - training_outputs[i][0];
                
            // back propagation
            
            // compute change in output weights
            double deltaOutput[numOutputs];

            for (int j = 0; j < numOutputs; j++) {
                double error = (training_outputs[i][j] - outputLayer[j]);
                deltaOutput[j] = error * derivative_sigmoid(outputLayer[j]);
            }

            // compute change in hidden weights
            double deltaHidden[numHiddenNodes];
            for (int j = 0; j < numHiddenNodes; j++) {
                double error = 0.0f;
                for (int k = 0; k < numOutputs; k++) {
                    error += deltaOutput[k] * outputWeights[j][k];
                }
                deltaHidden[j] = error * derivative_sigmoid(hiddenLayer[j]);
            }
                
            // Apply change in output weights
            for (int j = 0; j < numOutputs; j++) {
                outputBias[j] += deltaOutput[j] * learning_rate;
                for (int k = 0; k < numHiddenNodes; k++) {
                    outputWeights[k][j] += hiddenLayer[k] * deltaOutput[j] * learning_rate;
                }
            }
             
            // Apply change in hidden weights
            for (int j = 0; j < numHiddenNodes; j++) {
                hiddenLayerBias[j] += deltaHidden[j] * learning_rate;
                for (int k = 0; k < numInput; k++) {
                    hiddenWeights[k][j] += training_inputs[i][k] * deltaHidden[j] * learning_rate;
                }
            }
        }
    }
    return 0;
}

