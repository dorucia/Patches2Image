import os.path
import random
import torch
from PIL import Image
import numpy as np
from glob import glob
import scipy.io
import h5py

class Dataset():
    def __init__(self):
        self.opts = []
        self.num_imgs = 0
        self.img_list = []

    def initialize(self, opts):
        self.opts = opts
        self.num_imgs = 0
        self.db_name = opts.db_name
        self.edgeBoxResol = opts.edge_box_resol
        self.output_size = opts.output_size

        if self.db_name == 'celebA':
            # Load image list
            img_path = os.path.join(opts.dataset_root, 'celebA/img_align_celeba_png', "*.png")
            img_list = glob(img_path)
            self.img_list = np.array(sorted(img_list))
            self.num_imgs = len(self.img_list)

            # Load part BBoxes
            bbs = scipy.io.loadmat("celebA_allbbs.mat")['allbbs']
            changeRatio = float(self.output_size) / float(self.edgeBoxResol)
            bbs = np.floor(bbs * changeRatio).astype(np.int)

            self.bbs = bbs

        if self.db_name == 'celebAhq':
            # Load image list
            img_path = os.path.join(opts.dataset_root, 'celebA_hq/img/hq.hdf5')
            self.img_list = h5py.File(img_path, "r")
            self.img_list = self.img_list["data256x256"]
            self.num_imgs = len(self.img_list)

            # Load part BBoxes
            bbs = scipy.io.loadmat("/mnt/hi/dataset/celebA_hq/celebA_hq_allbbs256.mat")['allbbs']
            changeRatio = float(self.output_size) / float(self.edgeBoxResol)
            bbs = np.floor(bbs * changeRatio).astype(np.int)

            self.bbs = bbs

        elif self.db_name == 'compCar':
            print ('Not ready for compcar dataset ...')

    def __getitem__(self, index):
        index = list(sorted(index))
        img_path = self.img_list[index]
        bbs = self.bbs[index]
        return img_path, bbs

    def __len__(self):
        # return len(self.paths)
        return self.num_imgs

    def name(self):
        return 'Dataset'


