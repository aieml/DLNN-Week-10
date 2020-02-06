import numpy as np

x=np.matrix([[-1,10,20,-8],[1,23,53,53]])

array=np.where(x[0,:]>0)

print(array)
