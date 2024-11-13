import numpy as np
#pip opencv-python
import cv2
# Read image

#typewriter
#img = cv2.imread('../images/typewriter.jpg')
#img = cv2.imread('../images/fruit.jpg')
 

#equipments
#img = cv2.imread('../images/equipment2.jpg')

#buildings
#img = cv2.imread('../images/building1.jpg')
#img = cv2.imread('../images/building2.jpg')
#img = cv2.imread('../images/wc.jpg')

#pips
#img = cv2.imread('../images/pip1.jpg')
#img = cv2.imread('../images/pip2.jpg')

#solar
#img = cv2.imread('../images/solar2.jpg')
# img = cv2.imread('../images/solar3.jpg')
#img = cv2.imread('../images/solar4.jpg')
#img = cv2.imread('../images/solar5.jpg')
#img = cv2.imread('../images/farm1.jpg')
#img = cv2.imread('../images/farm2.jpg')
img = cv2.imread('../images/h1.jpg')
#img = cv2.imread('../images/h2.jpg')


print(img.shape)
#Image Dimensions : (400, 640, 3)  (height, width, number_of_channels).
#there are three color channels in the image.

all_rows = open('../model/synset_words.txt').read().strip().split("\n")

classes = [r[r.find(' ') + 1:] for r in all_rows]

net = cv2.dnn.readNetFromCaffe('../model/bvlc_googlenet.prototxt','../model/bvlc_googlenet.caffemodel')

blob = cv2.dnn.blobFromImage(img, 1, (224,224))
#blob = cv2.dnn.blobFromImage(image, scalefactor=1.0, size, mean, swapRB=True)
#SEE https://www.pyimagesearch.com/2017/11/06/deep-learning-opencvs-blobfromimage-works/

net.setInput(blob)

outp = net.forward()
#print(outp)
idx = np.argsort(outp[0])[::-1][:5]

for (i,id) in enumerate(idx):
    print('{}. {} ({}): Probability {:.3}%'.format(i+1, classes[id], id, outp[0][id]*100))
#for (i,c) in enumerate(classes):
#    if i==4:
#        break
#    print(i,c)

# Create window with freedom of dimensions
#cv2.namedWindow('Image', cv2.WINDOW_AUTOSIZE)  # By default,
cv2.namedWindow('Image', cv2.WINDOW_NORMAL) #you can resize window.

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#SHOW It with resize image
imS = cv2.resize(img, (960, 540))                    # Resize image
cv2.imshow("output", imS)                            # Show image
cv2.waitKey(0)                                      # Display the image infinitely until any keypress


from matplotlib import pyplot as plt

#img = cv2.imread('messi5.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()