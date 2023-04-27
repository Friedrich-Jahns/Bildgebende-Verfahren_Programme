import numpy as np


class N:
    def __init__(self,out):
        self.out = out




with open('Test/data.txt') as tf:
    data = np.genfromtxt(tf,delimiter=' ')
print(data)