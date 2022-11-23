

set -ex
python test.py --dataroot /home/rita/uwh_project/justin/datasets/SQUID_original/FolderA --name facades_pix2pix  --netG unet_256   --model test --norm batch  --gpu_ids 0
