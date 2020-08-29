import os
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector
import cv2
import sys
sys.path.append('D:\documents\darkflow\darkflow-master\python_files\car_bicyclewheel_bus')
from generate_xml import write_xml


print(os.getcwd())
os.chdir('D:\documents\darkflow\darkflow-master')
print(os.getcwd())
print('\n')





print(cv2.__file__)
print(cv2.__version__)
print('\n')



## global constants
img = None
tl_list = []
br_list = []
object_list = []


## Constants
image_folder = 'car_bicyclewheel_bus_dataset'
savedir = 'car_bicyclewheel_bus_annotations'
obj = ['car' , 'bicycle_wheel' , 'bus']



def line_select_callback(clk,rls):
    global tl_list
    global br_list
    global object_list
    tl_list.append((int(clk.xdata), int(clk.ydata)))
    br_list.append((int(rls.xdata), int(rls.ydata)))
    # object_list.append('bus')
    # object_name = input("Is it a car , bicycle wheel or bus? ")
    # if object_name == 'bicycle wheel':
    #     object_list.append('bicycle_wheel')
    #     tl_list.append((int(clk.xdata), int(clk.ydata)))
    #     br_list.append((int(rls.xdata), int(rls.ydata)))
    # if object_name == 'car':
    #     object_list.append('car')
    #     tl_list.append((int(clk.xdata), int(clk.ydata)))
    #     br_list.append((int(rls.xdata), int(rls.ydata)))
    # if object_name == 'bus':
    #     object_list.append('bus')
    #     tl_list.append((int(clk.xdata), int(clk.ydata)))
    #     br_list.append((int(rls.xdata), int(rls.ydata)))
    # else:
    #     print("wrong input")


def identify_object(event):
    global object_list
    if event.key == '1':
        object_list.append('car')
    if event.key == '2':
        object_list.append('bicycle_wheel')
    if event.key == '3':
        object_list.append('bus')



def onkeypress(event):
    global object_list
    global tl_list
    global br_list
    global img
    if event.key == 'q':
        print(object_list)
        print(tl_list)
        print(br_list)
        write_xml(image_folder, img, object_list, tl_list, br_list, savedir)
        tl_list = []
        br_list = []
        object_list = []
        img = None
        plt.close()



def toggle_selector(event):
    toggle.set_active(True)
        

if __name__ == '__main__':
    for n,image_file in enumerate(os.scandir(image_folder)):
        img = image_file
        fig,axs = plt.subplots(1)
        image = cv2.imread(img.path)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        axs.imshow(image)

        toggle = RectangleSelector(
            axs, line_select_callback,
            drawtype='box', useblit=True,
            button=[1], minspanx=5, minspany=5,
            spancoords='pixels', interactive=True
        )

        bbox = plt.connect('key_press_event', toggle_selector)
        identify = plt.connect('key_press_event',identify_object)
        key = plt.connect('key_press_event', onkeypress)
        plt.show()
