__file__ = 'fouriertransformation.py'
import pathlib
import scipy.fftpack as fft 
from skimage import color
from skimage import io
from matplotlib import pyplot as plt



def fourier(img):
    return fft.rfft(x=img, axis=1)


try:
    Image_Name = input("Image_Name:")
    path = str(pathlib.Path(__file__).absolute().parent)+'/fourier/'+str(Image_Name)
    try:
        imgi = io.imread(path)[:,:,:3]
        imgg = color.rgb2gray(imgi)
    except:
        imgi = io.imread(path)
        imgg = color.rgb2gray(imgi)
except:
    print('Does not exist')
    exit()

transformed = fourier(imgg)

plt.imshow(transformed, cmap = "gray")
plt.savefig('fourier/transformed_'+str(Image_Name))
plt.show()


