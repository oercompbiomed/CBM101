
# according to wikipedia: 
# Two vectors, x and y, in an inner product space, V, 
# are orthogonal if their inner product ⟨ x , y ⟩ is zero

fst = pca.components_[0]
snd = pca.components_[1]

print(fst, snd)
np.inner(fst, snd)

# fst@snd also works
# as well does pca.components_ @ pca.components_, yielding the identity matrix