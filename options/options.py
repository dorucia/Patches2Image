import argparse
import os

class Options():
    def __init__(self):
        self.parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

        ### OPTIONS ###
        self.parser.add_argument('--epoch',         type=int, default=200)
        self.parser.add_argument('--learning_rate', type=float, default=0.0002)
        self.parser.add_argument('--beta1',         type=float, default=0.5)
        self.parser.add_argument('--batch_size',    type=int, default=16)
        self.parser.add_argument('--image_size',    type=int, default=256)
        self.parser.add_argument('--output_size',   type=int, default=256)
        self.parser.add_argument('--c_dim',         type=int, default=3)
        self.parser.add_argument('--df_dim',        type=int, default=64)
        self.parser.add_argument('--z_dim',         type=int, default=256)
        self.parser.add_argument('--part_embed_dim', type=int, default=256)
        self.parser.add_argument('--num_conv_layers', type=int, default=6)
        self.parser.add_argument('--edge_box_resol', type=int, default=256)
        self.parser.add_argument('--is_train',      default=True)
        self.parser.add_argument('--is_crop',       default=False)
        self.parser.add_argument('--cont_train', default=True)
        self.parser.add_argument('--start_epoch', default=42)
        self.parser.add_argument('--sample_dir',    default='/mnt/hi/code/KeyPatchGan_celebhq_log42_z256_dfdim128_epoch200_newloss/results/samples')
        self.parser.add_argument('--test_dir',      default='/mnt/hi/code/KeyPatchGan_celebhq_log42_z256_dfdim128_epoch200_newloss/results/test')
        self.parser.add_argument('--net_dir',      default='/mnt/hi/code/KeyPatchGan_celebhq_log42_z256_dfdim128_epoch200_newloss/nets')
        self.parser.add_argument('--num_tests',     type=int, default=128)
        self.parser.add_argument('--num_samples',   type=int, default=128)

        ### OPTIONS ###
        self.parser.add_argument('--use_gpu', default=True)
        self.parser.add_argument('--gpu_id', default=0)
        self.parser.add_argument('--visdom_port', type=int, default=8097)
        self.parser.add_argument('--random_seed', default=1004)

        ### DATABASE OPTIONS ###
        self.parser.add_argument('--db_name', default='celebAhq')
        self.parser.add_argument('--dataset_root', default='/mnt/hi/dataset/')


    def parse(self):
        self.opt = self.parser.parse_args()
        args = vars(self.opt)
        for k,v in sorted(args.items()):
            print('%s: %s' %(str(k), str(v)))
        return self.opt
