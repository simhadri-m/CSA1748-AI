import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of sigmoid activation function
def sigmoid_derivative(x):
    return x * (1 - x)

# Neural Network class
class FeedForwardNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights with random values
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        self.weights_input_hidden = np.random.uniform(-1, 1, (self.input_size, self.hidden_size))
        self.weights_hidden_output = np.random.uniform(-1, 1, (self.hidden_size, self.output_size))
        
        self.bias_hidden = np.random.uniform(-1, 1, (1, self.hidden_size))
        self.bias_output = np.random.uniform(-1, 1, (1, self.output_size))

    def forward(self, X):
        self.input_layer = X
        self.hidden_layer = sigmoid(np.dot(self.input_layer, self.weights_input_hidden) + self.bias_hidden)
        self.output_layer = sigmoid(np.dot(self.hidden_layer, self.weights_hidden_output) + self.bias_output)
        return self.output_layer

    def backward(self, X, y, learning_rate=0.01):
        output_error = y - self.output_layer
        output_delta = output_error * sigmoid_derivative(self.output_layer)

        hidden_error = np.dot(output_delta, self.weights_hidden_output.T)
        hidden_delta = hidden_error * sigmoid_derivative(self.hidden_layer)

        # Update weights and biases
        self.weights_hidden_output += np.dot(self.hidden_layer.T, output_delta) * learning_rate
        self.bias_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate

        self.weights_input_hidden += np.dot(X.T, hidden_delta) * learning_rate
        self.bias_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate

    def train(self, X, y, epochs=10000, learning_rate=0.01):
        for _ in range(epochs):
            self.forward(X)
            self.backward(X, y, learning_rate)

# Example usage
if __name__ == "__main__":
    # Define input features and labels
    X = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]])
    y = np.array([[0],
                  [1],
                  [1],
                  [0]])

    # Create and train the neural network
    nn = FeedForwardNeuralNetwork(input_size=2, hidden_size=4, output_size=1)
    nn.train(X, y, epochs=10000, learning_rate=0.1)

    # Test the neural network
    predictions = nn.forward(X)
    print("Predictions:")
    print(predictions)
