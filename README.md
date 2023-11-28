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
    |--lanes_3D
|--evaluation
|--data
```
## Object_Annotation

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
image_id: Number of the image, from 00 to 79
intrinsic: 3x3 intrinsic matrix
sensor_name: back_camera, front_camera, front_left_camera, front_right_camera,
	     left_camera, right_camera
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

## Lane_Annotation
## Evaluation
