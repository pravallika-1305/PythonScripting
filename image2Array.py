from matplotlib import image
from matplotlib import pyplot
# load image as pixel array
data = image.imread('toConvert.jpg')
# summarize shape of the pixel array
print(data.dtype)
print(data.shape)
# display the array of pixels as an image
pyplot.imshow(data)
pyplot.show()
