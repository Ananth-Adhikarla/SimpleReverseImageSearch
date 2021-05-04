import os
from os import walk
import pickle
from cv2 import cv2
import matplotlib.pyplot as plt
import common

# load the query image and show it
queryImage = cv2.imread(common.fileName)
# create a window named query of dimensions 2.5,2.5 
plt.figure("QUERY",figsize=(2.5,2.5))
# convert image from opencv BGR to matplotlib RGB color space
img = cv2.cvtColor(queryImage,cv2.COLOR_BGR2RGB)
# display the image
plt.imshow(img, interpolation='nearest', aspect='auto')
print("query image is : ", common.fileName)

queryImageDescriptors = common.describe(queryImage)

# load the imageDescriptors perform the search
imageDescriptors = pickle.loads(open(common.saveName, "rb").read())

results = common.findsimilarimages(imageDescriptors,queryImageDescriptors)

# stores the top N images and score value - closer to 0 better match
top_images = []
# stores the top N images with full path used to open images
image_list = []

for j in range(0, 30):
    
    top_images.append(results[j])


for i in range(len(top_images)):
    
    imageScore = top_images[i][1]
    imageName = top_images[i][0]
    for path, subdirs, files in os.walk(common.path):
        for name in files:  
            imagePath = os.path.join(path,imageName)
            # use break since we want to get name once and exit the loop
            break
        
    result = cv2.imread(imagePath)
    #print("imageDescriptors: "+ str(i) + " Image Name: " + imageName + " Image Score: " +str(imageScore))
    image_list.append([result])


for i in range(len(image_list)):

    # adjust spacing between images shown in window
    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0.025, wspace = 0.025)
    
    # create a window called results and image size of 10,10
    plt.figure("RESULTS",figsize=(10,10))
    
    # create a subplot of 6 rows and 5 colums ( 30 images ) with the index greater than current number
    plt.subplot(6,5,i+1 )
    
    # convert image from opencv BGR to matplotlib RGB color space
    img = cv2.cvtColor(image_list[i][0],cv2.COLOR_BGR2RGB)
    
    # show image
    plt.imshow(img, interpolation='nearest', aspect='auto')
    
    # this sets the x,y labels,values of images to be turned off
    plt.xticks([])
    plt.yticks([])
    
plt.show()

image_list.clear()
