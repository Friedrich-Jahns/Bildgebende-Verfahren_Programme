import numpy as np
from pathlib import Path


dat = Path("Test/data.txt")
dat.touch()
nf = open(dat,"w")



for i in np.arange(0,10):
    for j in np.arange(3):
        nf.write(str(np.random.randint(2)))
        if j == 2:
            break
        else:
            nf.write('\t')

    nf.write('\n')

nf.close()