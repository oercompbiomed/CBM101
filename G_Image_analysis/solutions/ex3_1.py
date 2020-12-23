
def display_multispectral_image(data, mask, sl, scale = 300):
    """
    data  - 4D multispectral image data
    mask  - 3D ROI mask
    sl - slice number to be displayed
    scale - scaling factor for the superposition of the 0/1 ROI tumor mask (default value 300)
    """
    fig, axes = plt.subplots(2,2, figsize=(10,10))
    ax = axes.ravel()
    for k, ch in enumerate(chn_names):
        ax[k].imshow(data[:, :, sl, k].T + 300*mask[:,:,sl].T, cmap='gray', origin='lower')
        ax[k].set_title(ch)
        ax[k].set(xlabel="")
        ax[k].axis('off')
    plt.suptitle('The multispectral MRI slice %d with the ROI mask' % sl) 
    plt.tight_layout
    plt.show()
    
    
display_multispectral_image(data, mask, 10 )