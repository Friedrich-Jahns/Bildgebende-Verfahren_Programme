import numpy as np

def boxkernelsize(x):
    global ksn, kernelsize
    kernelsize = x
    if kernelsize%2==1:
        ksn = int((kernelsize-1)/2)
    else:
        raise ValueError('Kernelsize has to be an odd Number!')




def neighbours(a,b,mat,s):
    neighbors = [mat[i][j] for i in range(a-s, a+s+1) for j in range(b-s, b+s+1)]
    return neighbors




def mirror_padding(img,ksn):
    m2 = np.flipud(img)
    m2o = m2[-ksn:,:]
    m2u = m2[:ksn,:]
    m1 = np.fliplr(m2)
    m1ol=m1[-ksn:,-ksn:]
    m1ul=m1[:ksn,-ksn:]
    m1ur=m1[:ksn,:ksn]
    m1or=m1[-ksn:,:ksn]
    m3 = np.fliplr(img)
    m3l= m3[:,-ksn:]
    m3r= m3[:,:ksn]

    imgn=np.zeros((len(img)+2*ksn,len(img[0])+2*ksn))
    imgn[0:ksn,0:ksn]=m1ol
    imgn[ksn:-ksn,0:ksn]=m3l
    imgn[-ksn:,:ksn]=m1ul
    imgn[-ksn:,ksn:-ksn]=m2u
    imgn[-ksn:,-ksn:]=m1ur
    imgn[ksn:-ksn,-ksn:]=m3r
    imgn[0:ksn,-ksn:]=m1or
    imgn[0:ksn,ksn:-ksn]=m2o
    imgn[ksn:-ksn,ksn:-ksn]=img
    return imgn



    