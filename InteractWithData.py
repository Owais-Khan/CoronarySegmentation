import vtk
from vmtk import vmtkscripts

def RenderImage(FileName,Image):
	Renderer=vmtkscripts.vmtkImageViewer()
	Renderer.Image=Image
	Renderer.Execute()

