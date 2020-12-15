
# this one takes arbitrary many inputs
def perceptron(inputs, weights, b):
    s = sum([i*w for i,w in zip(inputs, weights)])
    return activation(s, b)