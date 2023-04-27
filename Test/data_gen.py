import numpy as np
from pathlib import Path


dat = Path("Test/data.txt")
dat.touch()
nf = open(dat,"w")

for i in np.arange(0,10):
    nf.write(str(np.random.randint(2,size=3))+'\n')


nf.close()