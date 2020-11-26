def plot(k):
    plt.imshow(X[k].reshape(8,8), cmap='gray')
    plt.title(f"Number = {y[k]}")
    plt.show()