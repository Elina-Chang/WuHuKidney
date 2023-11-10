import os
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

# 设置包含多个子文件夹的父文件夹路径
parent_folder = "/MRIData/WuHuKidney/OtherCentersData/GeJiShan/XianSeXiBaoLiu_nii"

# 初始化分辨率和强度范围的列表
resolutions_img = []
intensity_ranges_img = []
resolutions_roi = []
intensity_ranges_roi = []

# 循环遍历每个子文件夹
for subdir in tqdm(os.listdir(parent_folder)):
    subdir_path = os.path.join(parent_folder, subdir)
    
    # 确保是文件夹
    if os.path.isdir(subdir_path):
        # 初始化子文件夹内的.nii.gz文件列表
        for file in os.listdir(subdir_path):
            if file.endswith('.nii.gz') and 'src' in file:
                img=nib.load(os.path.join(subdir_path, file))
                resolution = img.header.get_zooms()
                resolutions_img.append(resolution)
                data = img.get_fdata()
                intensity_range = (data.min(), data.max())
                intensity_ranges_img.append(intensity_range)
            elif file.endswith('.nii.gz') and 'cRCC' in file:
                roi=nib.load(os.path.join(subdir_path, file))
                resolution = roi.header.get_zooms()
                resolutions_roi.append(resolution)
                data = roi.get_fdata()
                intensity_range = (data.min(), data.max())
                intensity_ranges_roi.append(intensity_range)
        
        
# 转换为NumPy数组
resolutions_img = np.array(resolutions_img)
resolutions_roi = np.array(resolutions_roi)
intensity_ranges_img = np.array(intensity_ranges_img)
intensity_ranges_roi = np.array(intensity_ranges_roi)

# 保存数组到文件
np.save('resolutions_img.npy', resolutions_img)
np.save('resolutions_roi.npy', resolutions_roi)
print(intensity_ranges_img)
np.save('intensity_ranges_img.npy', intensity_ranges_img)
np.save('intensity_ranges_roi.npy', intensity_ranges_roi)