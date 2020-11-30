
## scale and fit on the scaled data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
pred = KMeans(4).fit_predict(X_scaled)

# plotting
xmin,ymin,xmax,ymax = *X_scaled.min(0), *X_scaled.max(0) # the "*" just unpacks the values, not multiplication
plt.scatter(X_scaled[:,0],X_scaled[:,1], c=pred)
plt.xlim(xmin,xmax)
plt.ylim(ymin,ymax)
plt.title('KMeans with scaling')