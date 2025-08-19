Author: Paritosh Parmar (https://github.com/ParitoshParmar)
Code used in the following, also if you find it useful, please consider citing the following:

@inproceedings{parmar2019and,
  title={What and How Well You Performed? A Multitask Learning Approach to Action Quality Assessment},
  author={Parmar, Paritosh and Tran Morris, Brendan},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  pages={304--313},
  year={2019}
}

Set the options in opts.py file, and train_test files.

Sports-1M pretrained C3D weights available from here: http://imagelab.ing.unimore.it/files/c3d_pytorch/c3d.pickle
> wget http://imagelab.ing.unimore.it/files/c3d_pytorch/c3d.pickle
Must save c3d.pickle in the MTL-AQA_code_release directory


UNLV EE AI Server Notes
08/2025 Use Conda Pack to manage libraries since CUDA 10.0 etc. no longer supported by conda
https://datascience.stackexchange.com/questions/24093/how-to-clone-python-working-environment-on-another-machine

Install
> conda install -c conda-forge conda-pack
Backup
> conda pack -n <my_env> -o <out_name.tar.gz>
Restore
> mkdir -p <my_env>
> tar -xzf <out_name.tar.gz> -C <my_env>
This should work if you create the environment and untar inside of your miniconda installation
     ~/miniconda/envs

out_name.tar.gz = /home/morrisb4/code/MTL-AQA/mtl-aqa.tar.gz

> conda env create -n <my_env> --file environment.yml
