
# initialize some random weights
w1, w2, b = .6, .1, 1

fig = plt.figure(figsize=(14,14))

epochs=60  # number of epochs
fr=10      # the number of epochs between plots 
j=0 


for i in range(epochs):

    # train a single epoch and update accordingly
    w1, w2, b = train(perceptron, X, y, [w1, w2], b) 
    
    if i%fr == 0: 
        j += 1
        fig.add_subplot(5, 2, j); 
        plt.title(f'epoch = {i+10}')
        plot_decision(perceptron, X, y, [w1, w2], b)