set -ex
python train.py --dataroot /home/rita/uwh_project/Datasets/Underwater_PairedData256_filtered  --name color_pix2pix  --model colorization --gpu_ids 1 --lambda_L1 100 --norm batch --pool_size 0 
