
# for RGB
wrong_lbl = np.all(train_msk == [0,0,0], axis=2)
train_msk[wrong_lbl] = [255,255,255]

# for grayscale
wrong_lbl = (train_msk_grey == 0)
train_msk_grey[wrong_lbl] = 255