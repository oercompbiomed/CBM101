
# this one takes exactly 3 inputs
def perceptron(inputs, weights, b):
    in1, in2 = inputs
    w1, w2 = weights
    s = in1*w1 + in2*w2
    return activation(s, b)