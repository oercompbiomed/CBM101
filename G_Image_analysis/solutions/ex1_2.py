targ = 1 - np.all(train_msk == [255,255,255], axis=2).astype(np.uint8)
targ_roi = 1 - np.all(roi_msk == [255,255,255], axis=2).astype(np.uint8)
print('train_msk.shape', train_msk.shape)
print('targ.shape', targ.shape)