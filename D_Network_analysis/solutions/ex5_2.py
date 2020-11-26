d = np.sqrt(netmats.shape[1]).astype(np.int)
print(d)
netmats = netmats.reshape(netmats.shape[0], d,d)