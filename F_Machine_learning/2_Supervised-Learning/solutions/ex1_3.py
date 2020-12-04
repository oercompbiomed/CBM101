
preds = model.predict(X_test)

# element-wise comparison of numpy arrays
print(preds == y_test)

#accuracy
print('Accuracy:')
print(np.sum(preds == y_test) / preds.shape[0])