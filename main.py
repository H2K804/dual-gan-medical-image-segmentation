import argparse
import os
import scipy.misc
import numpy as np

from model import DualNet
import tensorflow as tf

parser = argparse.ArgumentParser(description='Argument parser')
""" Arguments related to network architecture"""
#parser.add_argument('--network_type', dest='network_type', default='fcn_4', help='fcn_1,fcn_2,fcn_4,fcn_8, fcn_16, fcn_32, fcn_64, fcn_128')
parser.add_argument('--image_size', dest='image_size', type=int, default=256, help='size of input images (applicable to both A images and B images)')
parser.add_argument('--fcn_filter_dim', dest='fcn_filter_dim', type=int, default=64, help='# of fcn filters in first conv layer')
parser.add_argument('--A_channels', dest='A_channels', type=int, default=3, help='# of channels of image A')
parser.add_argument('--B_channels', dest='B_channels', type=int, default=3, help='# of channels of image B')

"""Arguments related to run mode"""
parser.add_argument('--phase', dest='phase', default='train', help='train, test')

"""Arguments related to training"""
parser.add_argument('--loss_metric', dest='loss_metric', default='L1', help='L1, or L2')
parser.add_argument('--niter', dest='niter', type=int, default=30, help='# of iter at starting learning rate')
parser.add_argument('--lr', dest='lr', type=float, default=0.00005, help='initial learning rate for adam')#0.0002
parser.add_argument('--beta1', dest='beta1', type=float, default=0.5, help='momentum term of adam')
parser.add_argument('--flip', dest='flip', type=bool, default=True, help='if flip the images for data argumentation')
parser.add_argument('--dataset_name', dest='dataset_name', default='facades', help='name of the dataset')
parser.add_argument('--epoch', dest='epoch', type=int, default=50, help='# of epoch')
parser.add_argument('--batch_size', dest='batch_size', type=int, default=1, help='# images in batch')
parser.add_argument('--lambda_A', dest='lambda_A', type=float, default=20.0, help='# weights of A recovery loss')
parser.add_argument('--lambda_B', dest='lambda_B', type=float, default=20.0, help='# weights of B recovery loss')

"""Arguments related to monitoring and outputs"""
parser.add_argument('--save_freq', dest='save_freq', type=int, default=50, help='save the model every save_freq sgd iterations')
parser.add_argument('--checkpoint_dir', dest='checkpoint_dir', default='./checkpoint', help='models are saved here')
parser.add_argument('--sample_dir', dest='sample_dir', default='./sample', help='sample are saved here')
parser.add_argument('--test_dir', dest='test_dir', default='./test', help='test sample are saved here')

args = parser.parse_args()

def main(_):
    if not os.path.exists(args.checkpoint_dir):
        os.makedirs(args.checkpoint_dir)
    if not os.path.exists(args.sample_dir):
        os.makedirs(args.sample_dir)
    if not os.path.exists(args.test_dir):
        os.makedirs(args.test_dir)

    with tf.Session() as sess:
        model = DualNet(sess, image_size=args.image_size, batch_size=args.batch_size,\
                        dataset_name=args.dataset_name,A_channels = args.A_channels, \
						B_channels = args.B_channels, flip  = (args.flip == 'True'),\
                        checkpoint_dir=args.checkpoint_dir, sample_dir=args.sample_dir,\
						fcn_filter_dim = args.fcn_filter_dim,\
						loss_metric=args.loss_metric, lambda_B=args.lambda_B, \
						lambda_A= args.lambda_A)

        if args.phase == 'train':
            model.train(args)
        else:
            model.test(args)

if __name__ == '__main__':
    tf.app.run()
