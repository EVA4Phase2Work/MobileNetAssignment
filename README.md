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

## Training and Test Logs:

  0%|          | 0/125 [00:00<?, ?it/s]

EPOCH: 0

Loss=0.8082740902900696 Batch_id=124 Accuracy=76.53: 100%|██████████| 125/125 [00:50<00:00,  2.46it/s]


Test set: Average loss: 0.0101, Accuracy: 1513/2000 (75.65%)

  0%|          | 0/125 [00:00<?, ?it/s]

EPOCH: 1

Loss=0.59430330991745 Batch_id=124 Accuracy=80.09: 100%|██████████| 125/125 [00:50<00:00,  2.49it/s]
  0%|          | 0/125 [00:00<?, ?it/s]


Test set: Average loss: 0.0102, Accuracy: 1513/2000 (75.65%)

EPOCH: 2

Loss=0.526368260383606 Batch_id=124 Accuracy=81.05: 100%|██████████| 125/125 [00:50<00:00,  2.49it/s]
  0%|          | 0/125 [00:00<?, ?it/s]


Test set: Average loss: 0.0083, Accuracy: 1597/2000 (79.85%)

EPOCH: 3

Loss=0.23713454604148865 Batch_id=124 Accuracy=81.30: 100%|██████████| 125/125 [00:49<00:00,  2.50it/s]
  0%|          | 0/125 [00:00<?, ?it/s]


Test set: Average loss: 0.0096, Accuracy: 1543/2000 (77.15%)

EPOCH: 4

Loss=0.3365696370601654 Batch_id=124 Accuracy=81.66: 100%|██████████| 125/125 [00:49<00:00,  2.51it/s]
  0%|          | 0/125 [00:00<?, ?it/s]


Test set: Average loss: 0.0103, Accuracy: 1523/2000 (76.15%)

EPOCH: 5

Loss=0.7676298022270203 Batch_id=124 Accuracy=81.08: 100%|██████████| 125/125 [00:49<00:00,  2.50it/s]
  0%|          | 0/125 [00:00<?, ?it/s]


Test set: Average loss: 0.0107, Accuracy: 1501/2000 (75.05%)

EPOCH: 6

Loss=0.4119861423969269 Batch_id=124 Accuracy=82.99: 100%|██████████| 125/125 [00:50<00:00,  2.50it/s]
  0%|          | 0/125 [00:00<?, ?it/s]


Test set: Average loss: 0.0098, Accuracy: 1533/2000 (76.65%)

EPOCH: 7

Loss=0.40560612082481384 Batch_id=124 Accuracy=83.51: 100%|██████████| 125/125 [00:50<00:00,  2.50it/s]
  0%|          | 0/125 [00:00<?, ?it/s]


Test set: Average loss: 0.0104, Accuracy: 1518/2000 (75.90%)

EPOCH: 8

Loss=0.43818700313568115 Batch_id=124 Accuracy=83.66: 100%|██████████| 125/125 [00:50<00:00,  2.49it/s]
  0%|          | 0/125 [00:00<?, ?it/s]


Test set: Average loss: 0.0087, Accuracy: 1571/2000 (78.55%)

EPOCH: 9

Loss=0.7182902693748474 Batch_id=124 Accuracy=83.03: 100%|██████████| 125/125 [00:50<00:00,  2.46it/s]
  0%|          | 0/125 [00:00<?, ?it/s]


Test set: Average loss: 0.0094, Accuracy: 1549/2000 (77.45%)

EPOCH: 10

Loss=0.4431827664375305 Batch_id=124 Accuracy=83.72: 100%|██████████| 125/125 [00:50<00:00,  2.49it/s]
  0%|          | 0/125 [00:00<?, ?it/s]


Test set: Average loss: 0.0085, Accuracy: 1562/2000 (78.10%)

EPOCH: 11

Loss=0.26292145252227783 Batch_id=124 Accuracy=82.97: 100%|██████████| 125/125 [00:50<00:00,  2.48it/s]
  0%|          | 0/125 [00:00<?, ?it/s]


Test set: Average loss: 0.0090, Accuracy: 1552/2000 (77.60%)

EPOCH: 12

Loss=0.44260045886039734 Batch_id=124 Accuracy=83.53: 100%|██████████| 125/125 [00:50<00:00,  2.49it/s]
  0%|          | 0/125 [00:00<?, ?it/s]


Test set: Average loss: 0.0090, Accuracy: 1566/2000 (78.30%)

EPOCH: 13

Loss=0.4930155575275421 Batch_id=124 Accuracy=83.65: 100%|██████████| 125/125 [00:50<00:00,  2.49it/s]
  0%|          | 0/125 [00:00<?, ?it/s]


Test set: Average loss: 0.0085, Accuracy: 1578/2000 (78.90%)

EPOCH: 14

Loss=0.3133634924888611 Batch_id=124 Accuracy=83.30: 100%|██████████| 125/125 [00:50<00:00,  2.49it/s]


Test set: Average loss: 0.0091, Accuracy: 1555/2000 (77.75%)

























