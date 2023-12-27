# pandaset_plus
## Dataset Description
The structure is as below:
```
|--annotations
  |--objects
    |--train
    |--test
  |--lanes
    |--lanes_2D
	|--front_camera
	|--back_camera
	|--front_left_camera
	|--front_right_camera
	|--left_camera
	|--right_camera
    |--lanes_3D
	|--world_coordinate
	|--camera_coordinate
	  |--front_camera
	  |--back_camera
	  |--front_left_camera
	  |--front_right_camera
	  |--left_camera
	  |--right_camera
|--devkit
|--data
```
Data of PandaSet can be downloaded from https://www.kaggle.com/datasets/pz19930809/pandaset/data
## Object Annotation

```
-------------------------------------------------------------
Sequences for test: ["004", "006", "008", "012", "014", "018", "020", "045", "047", "048", "050", "051", "055", "059",
                 "062", "063", "068", "074", "079", "085", "086", "091", "092", "093", "099", "100", "104"]
Other sequences are for training.
-------------------------------------------------------------

Label description:
keypoints: Coordinates of 8 key points in image
        6-----7
     5--+--4  |
     |  |  |  |rear
front|  |  |  |
     |  2--+--3
     1-----0
dimensions: Length, width, height
corners: 3D coordinates of 8 keypoints in camera coordinate system
yaw: yaw in camera coordinate system
location: 3D coordinates of center points in camera coordinate system
image_id: ID of the image, from 00 to 79
intrinsic: 3x3 intrinsic matrix
sensor_name: back_camera, front_camera, front_left_camera, front_right_camera,
	     left_camera, right_camera
occlusion: occlusion level [0, 1, 2], for evaluation (only in test set) 
category_name: Include below categories:
[
    "Car",
    "Other Vehicle - Uncommon",
    "Towed Object",
    "Cones",
    "Pedestrian",
    "Pickup Truck",
    "Personal Mobility Device",
    "Construction Signs",
    "Other Vehicle - Construction Vehicle",
    "Signs",
    "Motorcycle",
    "Semi-truck",
    "Medium-sized Truck",
    "Pedestrian with Object",
    "Bicycle",
    "Bus",
    "Temporary Construction Barriers",
    "Rolling Containers",
    "Train",
    "Animals - Other",
    "Pylons",
    "Tram / Subway",
    "Motorized Scooter",
    "Other Vehicle - Pedicab",
    "Road Barriers",
    "Emergency Vehicle",
    "Animals - Bird"
]
 
```

## Lane Annotation
Both 3D and 2D Lane Annotations are with the same format (3D array).  
  
1st dimension: Lanes.  
2nd dimension: Points for each lane.  
3rd dimension: x, y, z coordinate of each point.

3D lane annotations are presented both in world coordinate system and camera coordinate system.
### 3D Lane Annotation
[
  [
    [x<sub>1</sub>, y<sub>1</sub>, z<sub>1</sub>], [x<sub>2</sub>, y<sub>2</sub>, z<sub>2</sub>], ..., [x<sub>n</sub>, y<sub>n</sub>, z<sub>n</sub>]
  ]
]
### 2D Lane Annotation
[
  [
    [x<sub>1</sub>, y<sub>1</sub>], [x<sub>2</sub>, y<sub>2</sub>], ..., [x<sub>n</sub>, y<sub>n</sub>]
  ]
]
## Projection and Coordinate System Transfrom
Please refer to PandaSet devkit https://github.com/scaleapi/pandaset-devkit
## Evaluation
