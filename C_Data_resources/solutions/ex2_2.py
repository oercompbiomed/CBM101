
# example solution. 
# You are not expected to make a nice plotting function,
# you can simply call plt.imshow a number of times and observe

print(faces.DESCR) # this shows there are 40 classes, 10 samples per class
print(faces.target) #the targets i.e. classes
print(np.unique(faces.target).shape) # another way to see n_classes

X = faces.images
y = faces.target

fig = plt.figure(figsize=(16,5))
idxs = [0,1,2, 11,12,13, 40,41]
for i,k in enumerate(idxs):
    ax=fig.add_subplot(2,4,i+1)
    ax.imshow(X[k])
    ax.set_title(f"target={y[k]}")
    
# looking at a few plots shows that each target is a single person.