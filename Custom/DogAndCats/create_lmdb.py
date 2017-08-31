
'''
Title           :create_lmdb.py
Description     :This script divides the training images into 2 sets and stores them in lmdb databases for training and validation.
Author          :Aman
Date Created    :20170622
Date Modified   :20170623
version         :0.1
usage           :python create_lmdb.py
python_version  :2.7.11
'''

import os 
import glob
import random 
import numpy as np
import cv2 

import caffe
import caffe.proto import caffe_pb2
import lmdb

