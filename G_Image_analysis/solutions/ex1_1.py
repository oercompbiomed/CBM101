
aff1 = img1_ap.affine
aff1_new = aff1.copy()
aff1_new[2][1]=-1  # Change sign
img1_is = nib.Nifti1Pair(img1.get_data(), aff1_new)
plotting.plot_anat(img1_is, title="flash_060 (IS)")
plotting.show()