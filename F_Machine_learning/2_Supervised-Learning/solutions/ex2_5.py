
for k in [1, 7, 15]:
    clf = neighbors.KNeighborsClassifier(n_neighbors = k)
    clf.fit(X_train, y_train)
    plot_decision_boundary(clf, X_test, y_test)
plt.show()

# The decision boundary is more fine-grained for small Ks.