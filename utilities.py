import vtk
import numpy as np

############ Input/Output ##################
def ReadVTUFile(FileName):
	reader=vtk.vtkXMLUnstructuredGridReader()
	reader.SetFileName(FileName)
	reader.Update()
	return reader.GetOutput()

def ReadVTPFile(FileName):
	reader=vtk.vtkXMLPolyDataReader()
	reader.SetFileName(FileName)
	reader.Update()
	return reader.GetOutput()

def ReadVTIFile(FileName):
	reader = vtk.vtkXMLImageDataReader() 
	reader.SetFileName(FileName) 
	reader.Update()
	return reader.GetOutput()

def WriteVTUFile(FileName,Data):
	writer=vtk.vtkXMLUnstructuredGridWriter()
	writer.SetFileName(FileName)
	writer.SetInputData(Data)
	writer.Update()
        
def WriteVTUFile(FileName,Data):
	writer=vtk.vtkXMLPolyDataWriter()
	writer.SetFileName(FileName)
	writer.SetInputData(Data)


################ Direction Function ###########
#This function will extract the direction from a
#block of receptive field.
#def DirectionVector(Image,Point,BoxSize):
	



	






