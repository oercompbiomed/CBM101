
# one possible solution
# if it yields a bad result, rerun code

class KM():
    def __init__(self, k):
        self.k = k     
        
    def distances(self, X): 
        """Makes a distance matrix to the centroids of shape (n_samples x n_centroids)"""
        return np.vstack([np.sum((X-self.centroids[i,:])**2, axis=1) for i in range(self.k)]).T
    
    def assign(self, X): 
        """Selects the index of the distance matrix which has the smallest entry"""
        dist = self.distances(X)
        return np.argmin(dist, axis=1)
  
    def update(self, X):
        """Updates centroid to mean of its constituents. If it has no constituents, respawn randomly"""
        for j in range(self.k):
            new_c = X[self.y==j,:].mean(axis=0)
            if np.any(np.isnan(new_c)): 
                self.centroids[j,:] = np.random.uniform(X.min(0), X.max(0), X.shape[1])        
            else: self.centroids[j, :] = new_c

    def __call__(self, X):
        n, d = X.shape
        self._converged = False
        self.centroids = X[np.random.randint(0,n, self.k), :] # initialize by random selection of samples
        self.y = np.zeros(shape=n) # empty initialize
        
        while True: #repeat until convergence
            #old_centroids = self.centroids 
            old_y = self.y
            self.y = self.assign(X)
            if np.all(self.y == old_y): return self.y
            self.update(X)        
        return self.y


km = KM(5)
y = km(X)


plt.scatter(X[:,0], X[:,1], c=y)
plt.scatter(km.centroids[:,0], km.centroids[:,1], marker='x', s=150, c='red')