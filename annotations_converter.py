import os
import cv2
from lxml import etree
import xml.etree.cElementTree as ET
import pandas as pd
# from csv import reader

os.chdir('D:\documents\darkflow\darkflow-master')

def txt_to_xml(datasetfolder,savedir,img,txtfiledir,all_objects_inorder):
    if not os.path.isdir(savedir):
        os.mkdir(savedir)

    image = cv2.imread(img.path)
    height,width,depth = image.shape

    txt_file = pd.read_csv(os.path.join(txtfiledir,img.name.replace('jpg','txt')) , sep = ' ',header=None )

    object_name_list = []
    tl = []
    br = []
    for index , content in txt_file.iterrows():
        object_name_list.append(all_objects_inorder[int(content[0])])
        x_centre = width * content[1]
        y_centre = height * content[2]
        img_width = width * content[3]
        img_height = height * content[4]
        tl.append((x_centre - (img_width/2), y_centre - (img_height/2)))
        br.append((x_centre + (img_width/2), y_centre + (img_height/2)))

    annotation = ET.Element('annotation')
    ET.SubElement(annotation,'folder').text = datasetfolder
    ET.SubElement(annotation, 'filename').text = img.name
    ET.SubElement(annotation, 'segmented').text = '0'
    size = ET.SubElement(annotation,'size')
    ET.SubElement(size, 'width').text = str(width)
    ET.SubElement(size, 'height').text = str(height)
    ET.SubElement(size, 'depth').text = str(depth)
    for obj, topl, botr in zip(object_name_list, tl, br):
        ob = ET.SubElement(annotation, 'object')
        ET.SubElement(ob, 'name').text = obj
        ET.SubElement(ob, 'pose').text = 'Unspecified'
        ET.SubElement(ob, 'truncated').text = '0'
        ET.SubElement(ob, 'difficult').text = '0'
        bbox = ET.SubElement(ob, 'bndbox')
        ET.SubElement(bbox, 'xmin').text = str(topl[0])
        ET.SubElement(bbox, 'ymin').text = str(topl[1])
        ET.SubElement(bbox, 'xmax').text = str(botr[0])
        ET.SubElement(bbox, 'ymax').text = str(botr[1])

    xml_str = ET.tostring(annotation)
    root = etree.fromstring(xml_str)
    xml_str = etree.tostring(root, pretty_print=True)

    save_path = os.path.join(savedir, img.name.replace('jpg', 'xml'))

    with open(save_path, 'wb') as temp_xml:
        temp_xml.write(xml_str)



if __name__ == '__main__':
    """
    for testing
    """

    folder = 'car_bicyclewheel_bus_dataset'
    img = [im for im in os.scandir('car_bicyclewheel_bus_dataset') if '000cf683df0119a3' in im.name][0]
    objects = ['car' , 'bicycle_wheel' , 'bus']
    savedir = 'annotations_testing'
    txt_to_xml(folder,savedir, img, 'D:\OIDv4_ToolKit\OID\Dataset\\train\Car_Bicyclewheel_bus', objects)




