import numpy as np

np_slugs = np.genfromtxt("seaslugs.txt",delimiter='\t',dtype=float,names=True)
print(np_slugs[0:3])