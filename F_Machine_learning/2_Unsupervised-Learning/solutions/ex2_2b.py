silhouette_scores = [silhouette_score(X, model.labels_)
                     for model in kmeans_per_k[1:]]