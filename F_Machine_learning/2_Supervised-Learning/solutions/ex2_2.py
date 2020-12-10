test_score = clf.score(X_test, y_test)
train_score = clf.score(X_train, y_train)
print(f"test score: {test_score} \ntrain score: {train_score}")

# notice that the train score is higher. This is because the test set is hitherto unseen, and thus more "difficult" to get right.