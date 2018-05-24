## Introduction

We use the DualGAN architecture proposed in [the paper](https://arxiv.org/pdf/1709.01872.pdf) to perform unsupervised image segmentation on Brain tumor scans.

# architecture of DualGAN

![architecture](https://github.com/duxingren14/DualGAN/blob/master/0.png)


## Dataset

The dataset used is available [here](https://figshare.com/articles/brain_tumor_dataset/1512427) collected by the authors of the [paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4598126/)


## Prerequisites

* Python (2.7 or later)

* numpy

* scipy

* NVIDIA GPU + CUDA 8.0 + CuDNN v5.1

* TensorFlow 1.0 or later

* MATLAB (for initial image processing)

## steps

* prepare images:
```
Run the prepareimgs.m MATLAB file.
Original images (domain A) will be generated in folder /datasets/med-image/train/A from the .mat files.
Segmented images (domain B) with highlighted tumor regions will be generated in folder /datasets/med-image/train/B.
```

* train the model:

```
To run Medical image segmentation dataset
python main.py --phase train --dataset_name med-image --epoch 45 --lambda_A 20.0 --lambda_B 20.0 --A_channels 3 --B_channels 3
```

* test the model:

```
python main.py --phase test --dataset_name med-image --image_size 256 --epoch 45 --lambda_A 20.0 --lambda_B 20.0
```
## Experimental Results
![result1.png](https://github.com/H2K804/dual-gan-medical-image-segmentation/blob/master/result1.png)



## Acknowledgements
Codes are built on the top of DualGAN-tensorflow implementation by the authors of the paper.
