set -ex
python train.py --dataroot /home/rita/uwh_project/justin/datasets/Underwater_PairedData256_filtered --name facades_pix2pix --model pix2pix --netG unet_256 --direction AtoB --lambda_L1 100 --dataset_mode aligned --norm batch --pool_size 0 --gpu_ids 0,1
