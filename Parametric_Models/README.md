# Parametric Models

We would run the SQUID method to obtain the depth map of the SQUID dataset. Afterward, we put the corresponding original input image and the depth map into the Sea-thru model and obtain the results.

## SQUID

### System Requirements:
The code requires MATLAB, and was tested on windows.


### Getting Started

1. Setup toolboxes
   - Download the toolbox from `https://github.com/pdollar/toolbox` into **"utils/toolbox/"**.
   - Download the toolbox from `https://github.com/pdollar/edges` into **"utils/edges/"**.

2. Put the **.TIF** image files on the **"images/Raw_TIF/"**.
2. Convert the **.TIF** image files to **.jpg** image files using `TIFtoJPG.py`
3. All the processed image are in the **"images/input/"** folder.
4. Run the file `main_underwater_restoration.m`
5. Results
   - The generated depth maps are stored in the **"image/output_depthmap/"** folder
   - The generated restored images are stored in the **"image/output_restored/"** folder

## Seathru

1. Change the directory to **Seathru_modified** folder by the command `cd Seathru_modified`
2. Run `seathru_modified.py` file by the command `python3  seathru_modified.py`
3. The result of sea-thru are stored in the **"image/output_seathru/"** folder