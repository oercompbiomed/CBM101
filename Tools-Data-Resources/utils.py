import itertools
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

#Confusion matrix. 
# Code adapted from http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html


def plot_confusion_matrix(cm, classes, ax=None,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues, labels=True):
    """
    This function prints and plots the confusion matrix.
    From 
    """
    
    if not ax: fig, ax = plt.subplots(figsize=(8,6))
    ax.imshow(cm, interpolation='nearest', cmap=cmap)
    tick_marks = np.arange(len(classes))
    plt.setp(ax, xticks=tick_marks, xticklabels=classes, 
             yticks=tick_marks, yticklabels=classes,
             title=title, xlabel="Predicted label", 
             ylabel="True label")
    #ax.set_xticks(tick_marks, classes, rotation=45)
    #plt.yticks(tick_marks, classes)

    if labels:
        fmt = 'd'
        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            ax.text(j, i, format(int(cm[i, j]), fmt),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    return ax

def plot_confusion_matrix_with_colorbar(cm, classes, figsize=(8,8), normalize=False, 
                                        title='Confusion matrix', 
                                        cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    (This function is copied from the scikit docs.)
    """
    fig, ax = plt.subplots(figsize=figsize)
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar(fraction=0.046, pad=0.04)
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
#    print(cm)
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j], horizontalalignment="center", color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True', fontsize=16)
    plt.xlabel('Predicted', fontsize=16)
    
    
# Modified from Geron

def plot_decision_boundary(clf, X, y, legend=False, plot_training=True, ax=None, figsize=(10,6)):
        
    if not ax: f, ax = plt.subplots(figsize=figsize)
    
    # Convert to numpy arrays in case X and y are data frames
    X, y = np.array(X), np.array(y)

    x1 = X[:,0] # First feature
    x2 = X[:, 1] # Second feature
    
    
    x1s = np.linspace(np.min(x1)-0.1*np.mean(x1), 1.1*np.max(x1), 100)
    x2s = np.linspace(np.min(x2)-0.1*np.mean(x2), 1.1*np.max(x2), 100)
    x1, x2 = np.meshgrid(x1s, x2s)
    X_new = np.c_[x1.ravel(), x2.ravel()]
    
    y_pred = clf.predict(X_new).reshape(x1.shape)
    
    custom_cmap = ListedColormap(['#fafab0','#9898ff','#a0faa0'])
    ax.contourf(x1, x2, y_pred, alpha=0.3, cmap=custom_cmap)

    custom_cmap2 = ListedColormap(['#7d7d58','#4c4c7f','#507d50'])
    ax.contour(x1, x2, y_pred, cmap=custom_cmap2, alpha=0.8)
    
    dots = ["yo", "bs", "g^"]
    
    if plot_training:
        for i in np.unique(y):
            
            ax.plot(X[:, 0][y==i], X[:, 1][y==i], dots[i], label=str(i))
    
    else:
        ax.set_xlabel(r"$x_1$", fontsize=18)
        ax.set_ylabel(r"$x_2$", fontsize=18, rotation=0)
    ax.legend(loc="lower right", fontsize=14)
    ax.set_title("Decision boundary")
    
    return ax