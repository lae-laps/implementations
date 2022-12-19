# neural network implementation

import math
import random
import matplotlib.pyplot as plt

e = 2.7182818284

num_input_nodes = 2
num_output_nodes = 1
num_hidden_nodes = 2
num_training_sets = 4

training_progression = []

def init_weights():
    return random.random()

def shuffle(array, n):
    if n > 1:
        i = 0
        while i < n - 1:
            i += 1
            j = int(i + random.randint(0, 1000) // (1000 / (n - i) + 1))          # 1000 is just a number used here
            t = array[j]
            array[j] = array[i]
            array[i] = t

def sigmoid(x):
    return 1 / (1 + (e ** -x))

def derivative_sigmoid(x):
    return x * (1 - x)

def train(learning_rate):
    hidden_layer = [0] * num_hidden_nodes
    output_layer = [0] * num_output_nodes

    hidden_layer_bias = [0] * num_hidden_nodes
    output_layer_bias = [0] * num_output_nodes

    hidden_layer_weights = [0] * num_input_nodes  
    for i in range(len(hidden_layer_weights)): hidden_layer_weights[i] = [0] * num_hidden_nodes
    output_layer_weights = [0] * num_hidden_nodes 
    for i in range(len(output_layer_weights)): output_layer_weights[i] = [0] * num_output_nodes
    
    print(hidden_layer_weights)
    print(output_layer_weights)

    # training data

    print("setting data")

    training_inputs = [
        [0.0, 0.0],
        [0.0, 0.1],
        [1.0, 0.0],
        [1.0, 1.1],
    ]
    training_outputs = [
        [0.0],
        [1.0],
        [1.0],
        [0.0],
    ]

    for i in range(num_input_nodes):
        for j in range(num_hidden_nodes):
            hidden_layer_weights[i][j] = init_weights()

    print(hidden_layer_weights)

    for i in range(num_hidden_nodes):
        for j in range(num_output_nodes):
            output_layer_weights[i][j - 1] = init_weights()

    print(output_layer_weights)

    for i in range(num_output_nodes):
        output_layer_bias[i] = init_weights()

    training_set_order = [0, 1, 2, 3]
    num_epochs = 10000

    # Training

    for epoch in range(num_epochs):
        print(f"training epoch {epoch}")
        shuffle(training_set_order, num_training_sets)
            
        for x in range(num_training_sets):
            i = training_set_order[x]
                
            # Forward pass
            # Compute hidden layer activation
            for j in range(num_hidden_nodes):
                activation = hidden_layer_bias[j]
                for k in range(num_input_nodes):
                    activation += training_inputs[i][k] * hidden_layer_weights[k][j]
                hidden_layer[j] = sigmoid(activation)
                    
            # compute output layer activation
            for j in range(num_output_nodes):
                activation = hidden_layer_bias[j] # this should be output_layer_bias but it doesnt work for some reason
                for k in range(num_hidden_nodes):
                    activation += hidden_layer[k] * output_layer_weights[k][j]
                output_layer[j] = sigmoid(activation)
                
            print(f"input: <{training_inputs[i][0]}> <{training_inputs[i][1]}> | output: <{round(output_layer[0], 16)}> | expected: {round(training_outputs[i][0], 16)} | output: {round(output_layer[0], 16)} | error: {round((output_layer[0] - training_outputs[i][0]), 16)} -> {round(((output_layer[0] - training_outputs[i][0]) * 100), 1)}%")
            training_progression.append(output_layer[0] - training_outputs[i][0])
                
            # Back Propagation
                
            # compute change in output weights
            delta_output = [0] * num_output_nodes
            for j in range(num_output_nodes):
                error = (training_outputs[i][j] - output_layer[j])
                delta_output[j] = error * derivative_sigmoid(output_layer[j]) 
                
            # compute change in hidden weights
            delta_hidden = [0] * num_hidden_nodes
            for j in range(num_hidden_nodes):
                error = 0.0
                for k in range(num_output_nodes):
                    error += delta_output[k] * output_layer_weights[j][k]
                delta_hidden[j] = error * derivative_sigmoid(hidden_layer[j])
                    
            # apply change in output weights
            for j in range(num_output_nodes):
                output_layer_bias[j] += delta_output[j] * learning_rate
                for k in range(num_hidden_nodes):
                    output_layer_weights[k][j] += hidden_layer[k] * delta_output[j] * learning_rate
                    
            # apply change in hidden weights
            for j in range(num_hidden_nodes):
                hidden_layer_bias[j] += delta_hidden[j] * learning_rate
                for k in range(num_input_nodes):
                    hidden_layer_weights[k][j] += training_inputs[i][k] * delta_hidden[j] * learning_rate
                    
                    
def view_training_progression_data(count):
    global training_progression
    base = []
    for i in range(len(training_progression)):
        base.append(i)

    plt.plot(base, training_progression)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.show()
    #plt.savefig(f"training_data/img{count}.png")
    plt.clf()
    training_progression = []

def main():
    while True:
        print('''
    . 1 - Normal Training 
    . 2 - Test Learning Rates
    . 3 - Exit
        ''')
        option = input("    >> ")
        try: 
            option = int(option)
        except Exception:
            continue
        if option == 1:
            lr = 0.5
            print("Training with learning rate set to {lr}")
            train(lr)
        elif option == 2:
            count = 0.1
            while count < 10:
                train(count)
                print(f" #### LEARNING RATE -> {count} ####")
                view_training_progression_data(int(count * 10))
                training_progression = []
                count += 0.1
        elif option == 3:
            exit()
        continue


main()
view_training_progression_data()
