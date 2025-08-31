##############################################
#
# The EyeGazer
#
# This takes images of people's faces and creates a visualization
# of the eye vector on theie face images
#
# Prerequisite: eye vectors are provided from the following repository
# https://github.com/TadasBaltrusaitis/OpenFace.git
#
##############################################
import argparse
import visualizer
from visualizer import EyeVisualizer

def main():
	parser = argparse.ArgumentParser(description='Eye Gazer')

	parser.add_argument('-f','--imagefile',action='store',help='File containing the image')
	parser.add_argument('-e','--eyeVec',action='store',help='Eye vector written as x y z')
	#parser.add_argument('--file',action='store')

	args=parser.parse_args()
	image=args.imagefile
	eye=args.eyeVec

	visualizeEye(image,eye)
	print "hello"


if __name__ == '__main__':
	main()
	
	
