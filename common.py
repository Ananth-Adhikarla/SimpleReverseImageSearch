from cv2 import cv2
import numpy as np
import os
from scipy import spatial


#-------------------------------------------------------------------------------
folder = r'/images'
path = os.getcwd() + folder

saveName = 'index.cpickle'
imageName = r'/1.jpg'

fileName = path + imageName
#--------------------------------------------------------------------------------


def describe(image):

	'''
	def calcHist(images, channels, mask, histSize, ranges, hist=None, accumulate=None)
	images : image array in a list 
	channels = R,G,B - 0,1,256
	mask not required - 8bit array 
	histSize = number of divisions per channel in histogram (8 Reds , 8 Blues , 8 Greens) 
				all data is sorted into this (8,8,8) is default - changing value will split
				data into more sections making it less effective
    ranges = range of each color value - lowest = 0 ( BLACK ) highest = 255 ( WHITE ) so 255 + 1 
    hist = not sure what this does default is none
    accumulate will pool all data on top of each other - leave it as none
	'''
	hist = cv2.calcHist([image], [0, 1, 2], None, [8,8,8], [0, 256, 0, 256, 0, 256])
	hist = cv2.normalize(hist,hist)
	
	return hist.flatten()

def findsimilarimages(myFile,queryImageDescriptors):

	sorted_dict = {}

	# loop over the list of images from pickle file
	for (name, imageDescriptors) in myFile.items():

		'''
		Chi-square distance calculation is a statistical method, 
		generally measures similarity between 2 feature matrices. 
		Such distance is generally used in many applications like similar image retrieval, 
		image texture, feature extractions etc.
		'''
		distance = chisquare_distance(imageDescriptors, queryImageDescriptors)
		#distance = cosine_distance(imageDescriptors, queryImageDescriptors)
	
		sorted_dict[name] = distance
		
	'''
	distance between 2 images that are same is 0.0
	so closer the value to 0 - better the match of image
	sort the dictionary ( ascending order ) to get values closer to 0
	'''
	sorted_dict = sorted(sorted_dict.items(), key=lambda item: item[1])

	return sorted_dict

'''
Chi-square distance calculation is a statistical method, generally measures similarity between 2 feature matrices
'''
def chisquare_distance(imageDescriptors, queryImageDescriptors, eps = 1e-10):

    distance = 0.5 * np.sum( [ ((a - b) ** 2) / (a + b + eps) for (a, b) in zip(imageDescriptors, queryImageDescriptors) ] )

    return distance

'''
Cosine distance refers to distance with dimensions representing features of the data object in a dataset
images are not matching properly with this method
'''
def cosine_distance(imageDescriptors, queryImageDescriptors):
    
    distance = 1 - spatial.distance.cosine(imageDescriptors, queryImageDescriptors)
    return distance
	