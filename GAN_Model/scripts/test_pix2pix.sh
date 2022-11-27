set -ex
python test.py --dataroot  /home/rita/uwh_project/justin/datasets/Seathru --name facades_pix2pix --model pix2pix --netG unet_256 --direction AtoB --dataset_mode aligned --norm batch --gpu_ids 0
