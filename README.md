# UNDERWATER IMAGE CORRECTION


The underwater image correction has both commercial and artistic use. Both parametric and end-to-end models are used to enhance the vision. We compare most successful parametric methods with state-of-the-art end-to-end GAN models, and discover that depth information is crucial for successful denoising strategies. We also explore performance of a new diffusion model on this task.

[![Original GAN SEATHRU](https://img.youtube.com/vi/jmMjNaARCiE/0.jpg)](https://youtu.be/jmMjNaARCiE  "Original GAN SEATHRU")

[![Original GAN SEATHRU](https://img.youtube.com/vi/BBAWEzrvduE/0.jpg)](https://youtu.be/BBAWEzrvduE  "Original GAN SEATHRU")




## Parametric methods:

### Sea-thru

Data preprocessing  


The original sea-thru code from https://github.com/hainh/sea-thru

@article{seathru,
author = {Akkaynak, Derya and Treibitz, Tali},
year = {2019},
month = {04},
title = {Sea-thru: A Method For Removing Water From Underwater Images},
journal = {Proceedings / CVPR, IEEE Computer Society Conference on Computer Vision and Pattern Recognition. IEEE Computer Society Conference on Computer Vision and Pattern Recognition}
}

The baseline images and depth estimations come from http://csms.haifa.ac.il/profiles/tTreibitz/datasets/sea_thru/index.html







### SQUID


## Deep Learning Methods:

### GAN Model

- Utilize out of the shelf pix2pix model. Treating the image enhancement problem as a style transfer. Training dataset in form of aligned input and ground truth data. 

@INPROCEEDINGS{8100115,
  author={Isola, Phillip and Zhu, Jun-Yan and Zhou, Tinghui and Efros, Alexei A.},
  booktitle={2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)}, 
  title={Image-to-Image Translation with Conditional Adversarial Networks}, 
  year={2017},pages={5967-5976},doi={10.1109/CVPR.2017.632}}



### Diffusion Model

- Utilize the out of the shelf Palette model for the translation. We modifed the gray-to-color generation setting of the original Palette to adapt to our task.

## Datasets
The baseline images and depth estimations for Sea-thru come from http://csms.haifa.ac.il/profiles/tTreibitz/datasets/sea_thru/index.html


## Results

Qualitative comparison between original images and the outputs returned by deep models: GAN and Diffusion as well as parametric Sea-thru and SQUID.

![Method comparison](https://github.com/khleeloo/uwh_project/blob/master/Comparison.png?raw=true "Method comparison")

