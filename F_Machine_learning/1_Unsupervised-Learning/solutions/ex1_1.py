
means = scaled.mean(axis=0) # axis 0 means rows
stds = scaled.std(axis=0)

print(np.allclose(means, 0))  # checks if all are 0 within an error threshold (floating point errors will always occur)
print(np.allclose(stds, 1)) # checks if all stds or equivalently variances are 1