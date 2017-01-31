from numpy import exp, array, random, dot

class NeuralNetwork():
    def __init__(self):
        #Seed the random number generator, sot it generaes the same numbers 
        #evertime the programs runs
        random.seed(1)

        #We model a single neuron, with 3 input connections and 1 output connection. 
        # we assign random weights to 3 X 1 matrix, with the values in the range -1 
        # to 1 and mean 0   
        self.synaptic_weights = 2 * random.random((3,1)) - 1

    #The sigmoid function, which describes an s shaped curve
    # we pass the weigtjed sum of the inputs through this function
    # to normalize them between 0 and 1
    def __sigmoid(self, x):
        return 1/ ( 1 + exp(-x))
    
    # The derivative of the Sigmoid function.
    # This is the gradient of the Sigmoid curve.
    # It indicates how confident we are about the existing weight.
    def _sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, traning_set_inputs, training_set_outputs, num_of_iterations):
        for iteration in range(num_of_iterations):
            # pass the training set through our neural net 
            output = self.predict(training_set_inputs)

            #calculate the error 
            error = training_set_outputs - output

            #multiply the error by the input ad again bu the gradient of the sigmoid curve
            adjustment = dot(training_set_inputs.T, error * self._sigmoid_derivative(output))
            
            self.synaptic_weights += adjustment


    def predict(self, inputs):
        return self.__sigmoid(dot(inputs, self.synaptic_weights))

if __name__ == '__main__':
    #initalise a single neuro neural network
    neural_network = NeuralNetwork()

    print ('Random starting synaptic weights')
    print(neural_network.synaptic_weights)


    #The training set, we have 4 examples, each consisting of 3 input values 
    # and 1 output value 
    training_set_inputs = array([[0,0,1], [1,1,1],[1,0,1],[0,1,1]])
    training_set_outputs = array([[0, 1, 1, 0]]).T

    #train the neural network using a training set .
    # Do it 10,000 times and make small adjustment each time 
    num_of_iterations = 10000
    neural_network.train(training_set_inputs, training_set_outputs, num_of_iterations)

    print('New synatpic weights after training:')
    print(neural_network.synaptic_weights)

    print('Predicting:')
    print(neural_network.predict(array([1, 0, 0])))