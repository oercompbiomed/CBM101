a = train_msk_grey.flatten()
unique, counts = np.unique(a, return_counts=True)
d = dict(zip(unique, counts))
sorted_by_counts = sorted(d.items(), key=lambda v: v[1], reverse=True)  # by second element
sorted_by_counts

# You could also make use of this one: np.bincount(a)