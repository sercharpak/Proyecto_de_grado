#Script to insert a DICOM image into a bigger all black image
# Inspired by: http://pydicom.readthedocs.io/en/stable/working_with_pixel_data.html
#Written by Sergio Daniel Hernandez Charpak

#Example:
#python changing_size_DICOM_images.py ../imagenes/Case_3/ ../imagenes/Case_3_crop/ 2
USAGE = "python changing_size_DICOM_images.py path/input_folder path/output_folder size_factor(float)"

#Imports
import numpy as np
import matplotlib.pyplot as plt
import dicom as dc
import glob as gl
import os as os
import sys as sys

#Method to insert the image in the center of an all black image of double dimensions
def doubingSize(input_file, output_file, size_factor):
    data = dc.read_file(input_file)
    array = data.pixel_array
    n_columns = data.Columns
    n_rows = data.Rows
    #New size
    new_n_columns = int(size_factor * n_columns)
    new_n_rows = int(size_factor * n_rows)
    #New array - all black
    new_array = np.zeros((new_n_rows, new_n_columns))
    #Inserting the image in the center
    for i in range(n_rows):
        for j in range(n_columns):
            new_array[int((new_n_rows -n_rows)/2)+ i, int((new_n_columns -n_columns)/2)+j] = array[i,j]
    #Changing to the correct dtype
    new_array = new_array.astype(np.uint16)
    #Preparing to save
    data.Columns = new_n_columns
    data.Rows = new_n_rows
    data.pixel_array = new_array
    data.PixelData = new_array.tostring()
    data.save_as(output_file)

#Verifing the amount of arguments
if(len(sys.argv)!=4):
    print "Please use correctly"
    print USAGE
    sys.exit()

#Defining the input and output folder
folder_input = sys.argv[1]
folder_output = sys.argv[2]
size_factor = float(sys.argv[3])
#Getting the file set
fileset = gl.glob(folder_input+"*")

#Looping in the files
for input_file in fileset:
    #Getting the name of the file without the path
    name = os.path.basename(input_file)
    output_file = folder_output + name
    doubingSize(input_file, output_file, size_factor)

#Visualize an image
#plt.imshow(test_data.pixel_array, cmap=plt.cm.bone)
#plt.show()
