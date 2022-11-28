# UNDERWATER IMAGE CORRECTION


The underwater image correction has both commercial and artistic use. Both parametric and end-to-end models are used to enhance the vision. We compare most successful parametric methods with state-of-the-art end-to-end GAN models, and discover that depth information is crucial for successful denoising strategies. We also explore performance of a new diffusion model on this task.

**Watch this**    
[![Original GAN SEATHRU Diffusion](https:/SJVx1dsXTSc/img.youtube.com/vi/SJVx1dsXTSc/0.jpg)](https://github.com/khleeloo/uwh_project/blob/master/WhatsApp%20Video%202022-11-24%20at%205.28.40%20PM.mp4?raw=true )


[![Original GAN SEATHRU Diffusion](https://img.youtube.com/vi/yElrHq4LtCA/0.jpg)](https://github.com/khleeloo/uwh_project/blob/master/WhatsApp%20Video%202022-11-24%20at%205.28.44%20PM.mp4?raw=true "Original GAN SEATHRU Diffusion")





## Parametric methods:

### Sea-thru

- Use a raw image and a depth map as input to remove water.

The original sea-thru code from https://github.com/hainh/sea-thru

``
@article{seathru,
author = {Akkaynak, Derya and Treibitz, Tali},
year = {2019},
month = {04},
title = {Sea-thru: A Method For Removing Water From Underwater Images},
journal = {Proceedings / CVPR, IEEE Computer Society Conference on Computer Vision and Pattern Recognition. IEEE Computer Society Conference on Computer Vision and Pattern Recognition}
}
``

The baseline images and depth estimations come from http://csms.haifa.ac.il/profiles/tTreibitz/datasets/sea_thru/index.html




### SQUID

- To generate depth maps and color restored images

The original sea-thru code from https://github.com/danaberman/underwater-hl

``
@inproceedings{UnderwaterHL,
title={Diving into Haze-Lines: Color Restoration of Underwater Images},
author={Berman, D. and Treibitz, T. and Avidan, S.},
booktitle={Proceedings of the British Machine Vision Conference},
publisher = {BMVA Press}, year={2017}, }
``


The dataset is come from http://csms.haifa.ac.il/profiles/tTreibitz/datasets/ambient_forwardlooking/index.html

## Deep Learning Methods:

### GAN Model

- Utilize out of the shelf **pix2pix** model. Treating the image enhancement problem as a style transfer. Training dataset in form of aligned input and ground truth data. 
- The link to the original model https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix

``
@INPROCEEDINGS{8100115,
  author={Isola, Phillip and Zhu, Jun-Yan and Zhou, Tinghui and Efros, Alexei A.},
  booktitle={2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)}, 
  title={Image-to-Image Translation with Conditional Adversarial Networks}, 
  year={2017},pages={5967-5976},doi={10.1109/CVPR.2017.632}}
``


### Diffusion Model

- Utilize the out of the shelf Palette model for the translation. We modifed the gray-to-color generation setting of the original Palette to adapt to our task.


## Datasets
**UWH Dataset** Dataset from underwater hockey games taken by gopro or underwater drone. The dataset is used in this work for evaluation and will be releaset upon completion.
**Sea-thru** The baseline images and depth estimations for Sea-thru come from http://csms.haifa.ac.il/profiles/tTreibitz/datasets/sea_thru/index.html    
**EUVP Dataset** The EUVP (Enhancing Underwater Visual Perception) dataset contains separate sets of paired and unpaired image samples of poor and good perceptual quality to facilitate supervised training of underwater image enhancement models. https://irvlab.cs.umn.edu/resources/euvp-dataset

**UIEB Dataset** Underwater Image Enhancement Benchmark (UIEB) including 950 real-world underwater images, 890 of which have the corresponding reference images. Paper: https://arxiv.org/abs/1901.05495   Data: https://li-chongyi.github.io/proj_benchmark.html



## Results

**Evaluation**: Evaluation code evaluate.py available in Metrics file based on https://github.com/xueleichen/PSNR-SSIM-UCIQE-UIQM-Python , available with preprocess.py for image preprocessing (in case of PSNR and SSIM images have to be resized to the same size and with the same number of channels)

Quantitative comparison of the different model performance.

![Results](https://github.com/khleeloo/uwh_project/blob/master/results.png?raw=true "Results")

Qualitative comparison between original images and the outputs returned by deep models: GAN and Diffusion as well as parametric Sea-thru and SQUID.

![Method comparison](https://github.com/khleeloo/uwh_project/blob/master/Comparison.png?raw=true "Method comparison")

## Other Repos and Methods

1. GAN based, no depthmap required   

**UGAN (Underwater GAN)**
Repo: https://github.com/cameronfabbri/Underwater-Color-Correction
    Dataset: https://irvlab.cs.umn.edu/resources
    

**Adaptive Weighted Multi-Discriminator CycleGAN for Underwater Image Enhancement**
Paper: https://www.mdpi.com/2077-1312/7/7/200

Use CycleGAN method for unsupervised image color correction. 
Dataset is basically just unpaired sets of clean & dirty underwater images.
NO Depth map required

**Underwater-GAN: Underwater Image Restoration via Conditional Generative Adversarial Network**
Paper: https://link.springer.com/chapter/10.1007/978-3-030-05792-3_7

 Synthesize the underwater turbid images by color manipulation of on-air-taken images

2. Depth-map involved 

**WaterGAN: Unsupervised Generative Network to Enable Real-Time Color Correction of Monocular Underwater Images**

Paper: https://ieeexplore.ieee.org/abstract/document/7995024
Repo & Dataset: https://github.com/kskin/WaterGAN)


**All-In-One Underwater Image Enhancement using Domain-Adversarial Learning**

Paper:http://openaccess.thecvf.com/content_CVPRW_2019/papers/UG2+%20Prize%20Challenge/Uplavikar_All-in-One_Underwater_Image_Enhancement_Using_Domain-Adversarial_Learning_CVPRW_2019_paper.pdf
Repo:https://github.com/TAMU-VITA/All-In-One-Underwater-Image-Enhancement-using-Domain-Adversarial-Learning

“Create” Paired dataset by distorting the original on-air-taken photos using the depth-map of the air-taken images. 




