import os
import sys
sys.path.append('D:\documents\darkflow\darkflow-master\python_files\car_bicyclewheel_bus')

from annotations_converter import txt_to_xml

dataset_folder = 'D:\documents\darkflow\darkflow-master\car_bicyclewheel_bus_dataset'
savedir = 'D:\documents\darkflow\darkflow-master\car_bicyclewheel_bus_annotations'
txtfiledir = 'D:\OIDv4_ToolKit\OID\Dataset\\train\Car_Bicyclewheel_bus'
object_list = ['car', 'bicycle_wheel','bus']

os.chdir('D:\documents\darkflow\darkflow-master')

for image_file in os.scandir(dataset_folder):
    txt_to_xml(dataset_folder,savedir,image_file,txtfiledir,object_list)

