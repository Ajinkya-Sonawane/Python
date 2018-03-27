'''
Matplotlib is a plotting library for Python which gives you wide variety of plotting methods.
You will see them in coming articles.
Here, you will learn how to display image with Matplotlib.
You can zoom images, save it etc using Matplotlib.


89
down vote
accepted
There is a slight difference in pixel ordering in OpenCV and Matplotlib.

OpenCV follows BGR order, while matplotlib likely follows RGB order.

So when you display an image loaded in OpenCV using pylab functions, you may need to convert it into RGB mode.
Below method demonstrate it:

'''
import cv2
from matplotlib import pyplot as plt

# Read the image
img = cv2.imread('a.png', 1)

# Split the pixels
b, g, r = cv2.split(img)

# merge the pixels in R,G,B order
img2 = cv2.merge([r, g, b])

plt.subplot(121);
plt.imshow(img)  # expects distorted color
plt.subplot(122);
plt.imshow(img2)  # expect true color
plt.show()
