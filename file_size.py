import os

def file_size(path):
""" show the total disk useage and path """
	total = os.path.getsize(path) 				#return the disk useage
	if os.path.isdir(path):       				#check if a directory
		for filename in os.listdir(path):		#return the file list
			child =os.path.join(path,filename)	
			total +=file_size(child)
	print ( total, path)
	return total

file_size("D:\python\program\\tutorial\\basics")

