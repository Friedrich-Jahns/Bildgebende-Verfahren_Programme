import numpy as np


class N:
    def __init__(self,out):
        self.out = out




with open('Test/data.txt') as tf:
    data = np.genfromtxt(tf,delimiter='\t')


data[1]
for i in range(10):
    for j in  