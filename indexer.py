'''
pickle package:
Python pickle module is used for serializing and de-serializing python object structures. 
The process to converts any kind of python objects (list, dict, etc.) into byte streams (0s and 1s) is called pickling 
or serialization or flattening or marshalling. We can converts the byte stream (generated through pickling) back into 
python objects by a process called as unpickling.

opencv package:
OpenCV is a huge open-source library for computer vision, machine learning, and image processing.
It can process images and videos to identify objects, faces, or even the handwriting of a human. 
When it is integrated with various libraries, such as Numpy which is a highly optimized library for numerical operations, 
then the number of weapons increases in your Arsenal i.e whatever operations one can do in Numpy can be combined with OpenCV.

'''

import pickle
from cv2 import cv2
import os
from os import walk
import common



'''
create a dictionary to store data in the format of key,value pairs
Key = imagename , value is normalized flattened array of image
'''

my_images = {}

'''
os.walk(path) creates a <generator object walk at 0x7f70c89592e0>
general syntax for using needs 3 output variable from 1 input
if path,subdirs is removed it does not work ( need to learn )
'''
for path, subdirs, files in os.walk(common.path):
    # for a list of files get the name of each file
	for name in files: 
		# Full path of file 
		#print(os.path.join(path, name)) 
		imagePath = os.path.join(path,name)
		
		'''
		cv2.imread() - reads an image - needs to be in current working directory or
		full path must be given such as imagepath - since images are in subdirectory
		'''
		image = cv2.imread(imagePath)

		'''
		common.describe computes a 3D histogram in the RGB colorspace
		then normalize the histogram so that images that are same but modified
		such as enlarged , rotated , cropped will be normalized to have the same histogram
		Normalization usually means transforming the data you are working with to a common frame of reference.
		return the histogram as 1D array ( smaller size)
		'''
		image_descriptors = common.describe(image)

		# store the image descriptors with image name as key
		my_images[name] = image_descriptors


# open our pickle file - saveName 
# The wb indicates that the file is opened for writing in binary mode.
f = open(common.saveName, "wb")
f.write(pickle.dumps(my_images))
f.close()


print("indexed " + str(len(my_images)) +" images")
