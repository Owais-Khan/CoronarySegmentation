import vtk
import numpy as np
import argparse

from utilities import *
from InteractWithData import *
class CoronarySegmentation():
	def __init__(self,Args):
		self.Args=Args
		self.Image=ReadVTIFile(self.Args.InputFileName) #Get Image Data
		self.Spacing=Image.GetSpacing()	#Get Image Spacing
		self.Radius=max(self.Spacing)
	def Main(self):
		RCA=[178,197,245]	
		print (dir(Image))
			
			
	
		
		exit(1)
if __name__=="__main__":
	#Description
	parser = argparse.ArgumentParser(description="This script will generate tecplot files from perfusion territory vtu files.")

	#Add arguments
	parser.add_argument('-ifile', '--InutputFileName', type=str, required=False, dest="InputFileName",help="The Input filename of the coronart CTA file in vtk format")
        
	args=parser.parse_args()
	args.InputFileName="../data/CABG3A.vti"
	CoronarySegmentation(args).Main()
