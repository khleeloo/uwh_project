#!/bin/bash

python  seathru.py \
    --image '/home/khleeloo/code/sea-thru/Raw/LFT_3374.NEF'  \
    --depth-map '/home/khleeloo/code/sea-thru/depthMaps/depthLFT_3374.tif' --output "output_3374.png" \
    --output-graphs --monodepth


