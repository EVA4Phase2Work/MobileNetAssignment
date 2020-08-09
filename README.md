# MobileNetAssignment
MobileNet Assignment

This assignment is about train mobilenet on a custom dataset of four types of images:
i. Large Quadcopter

ii. Small QuadCopter

iii. Winged Drones

iv. Flying Birds


## Dataset Creation
From the consolidated images, we did the following processing

-  Cleaned up Images which are of webp format
-  Clealed up some the images which do not look 
-  Made the Image dataset balanced with respect to all the classes

We created a directory hierachy of folders below and placed all the images of  classes to respective folders

train ----  LargeQuadcopters

      ----  SmallQuadcopters
      
      ----  WingedDrones
      
      ----  FlyingBirds
      
test  ----- LargeQuadcopters

      ----  SmallQuadcopters
      
      ----  WingedDrones
      
      ----  FlyingBirds
      
We did a split of 80:20 for train and test datasets


## Data Loader

Created separate Data Loaders for Train and Test. The workflow for Data Loader is as below:

![Flowchart](/doc_images/data_loader_flowchart.png)







