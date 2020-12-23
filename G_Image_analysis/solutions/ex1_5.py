def make_feature_matrix(k):
    '''
    Ex.
    A = make_feature_matrix(air)
    A.shape
    '''
    M = np.column_stack(
        (flash_chn[k == 1], 
         dess_chn[k == 1],
         fisp_chn[k == 1],
         psif_chn[k == 1]))
    return M

A = make_feature_matrix(air)
print('Noise in FLASH: %.2f (n=%d)' % (A[:,0].std(), A.shape[0]))
print('Noise in DESS : %.2f (n=%d)' % (A[:,1].std(), A.shape[0]))
print('Noise in FSIP : %.2f (n=%d)' % (A[:,2].std(), A.shape[0]))
print('Noise in PSIF : %.2f (n=%d)' % (A[:,3].std(), A.shape[0]))