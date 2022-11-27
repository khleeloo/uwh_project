set -ex
python train.py --dataroot /home/rita/uwh_project/Datasets//home/rita/uwh_project/Datasets/UWH_Showcase_video_frames/1_images \
--name facades_pix2pix --checkpoints_dir './checkpoints' \
--model pix2pix --netG unet_256 \
--direction AtoB --lambda_L1 100 \
--dataset_mode aligned \
--n_epochs 200 --norm batch --pool_size 0 \
--gpu_ids 1 --batch_size 16 --continue_train 
