
## Prerequisites

* Python (2.7 or later)

* numpy

* scipy

* NVIDIA GPU + CUDA 8.0 + CuDNN v5.1

* TensorFlow 1.0 or later

* unzip


# Getting Started
## steps

* train the model:

```
1. To run Sketch to photo training
python main.py --phase train --dataset_name sketch-photo --image_size 256 --epoch 45 --lambda_A 20.0 --lambda_B 20.0 --A_channels 1 --B_channels 1

2. To run Medical image segmentation dataset
python main.py --phase train --dataset_name med-image --epoch 45 --lambda_A 20.0 --lambda_B 20.0 --A_channels 3 --B_channels 3

3. To run the maps to aerial dataset
python main.py --phase train --dataset_name maps --epoch 45 --lambda_A 20.0 --lambda_B 20.0 --A_channels 3 --B_channels 3


```

* test the model:

```
python main.py --phase test --dataset_name sketch-photo --image_size 256 --epoch 45 --lambda_A 20.0 --lambda_B 20.0 --A_channels 1 --B_channels 1
```
