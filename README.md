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

train
      ----  LargeQuadcopters

      ----  SmallQuadcopters
      
      ----  WingedDrones
      
      ----  FlyingBirds
      
test 
     ----- LargeQuadcopters

      ----  SmallQuadcopters
      
      ----  WingedDrones
      
      ----  FlyingBirds
      
We did a split of 80:20 for train and test datasets. Created a zip file of dataset 

https://drive.google.com/file/d/1T-713QxUjAaGhARD_ledI1PWP6xfoK-f/view?usp=sharing


## Data Loader

Created separate Data Loaders for Train and Test. The workflow for Data Loader is as below:

![Flowchart](/doc_images/dataloader_flowchart.png)

We used two separate dataloaders for train and test. For each of dataloader:

- Created a map of class id and list of images
- Get the index for the image
- From index get the class_id and file_id
- Read the image file
- If there is any issue with image then take the next file_id


## How to handle different image size

The dataset contains different image sizes. To Handle this we used following data transformation

- Resize the image to 256
- Random crop the image so that final image is of size 2224x224


## Model

We used pretrained MobileNet Model and dit the following changes:

- In the last classification layer used 4 outputs
- Free all the layers except final classification 


## Training

For training we used:

- SGD Optimizer with lr=0.01, momentum=0.9
- StepSizeLR with step_size=6, gamma=0.1
- Batch Size: 32


## Training And Test Accuracy Plot

![Accuracy Plots](/doc_images/accuracy_plot.png)



## Misclassified Images (10 per class)

![Large Quadcopter](/doc_images/misclassified_images_large_quadcopter.png)
![Samll Quadcopter](/doc_images/misclassified_images_small_quadcopter.png)
![Winged Drone](/doc_images/misclassified_images_winged_drone.png)
![Flying Bird](/doc_images/misclassified_images_flying_bird.png)























