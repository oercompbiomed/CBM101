X_full = brca.data

X_train, X_test, y_train, y_test = train_test_split(X_full, y, test_size=0.2, random_state=0)
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


clf = neighbors.KNeighborsClassifier(n_neighbors=5)
clf.fit(X_train, y_train)

test_score = clf.score(X_test, y_test)
train_score = clf.score(X_train, y_train)
print(f"test score: {test_score} \ntrain score: {train_score}")