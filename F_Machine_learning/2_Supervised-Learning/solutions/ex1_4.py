
X2 = iris_dataset.data[:, :2]
y =  iris_dataset.target

# We split the two-features dataset into test and train as before
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y, random_state=42)