silhouette_scores = [silhouette_score(X, hierarchy.fcluster(Z, t, 'maxclust'))
                     for t in [2,3,4,5,6,7,8,9]]
plt.plot(range(2, 10), silhouette_scores, "bo-")