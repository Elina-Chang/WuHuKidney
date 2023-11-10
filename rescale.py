import os
import numpy as np
import SimpleITK as sitk
from tqdm import tqdm

def adjust_ww_wl(data,w_width=250,w_center=40): 
    val_min = w_center - (w_width / 2) 
    val_max = w_center + (w_width / 2) 
    data_adjusted = data.copy() 
    data_adjusted[data < val_min] = val_min 
    data_adjusted[data > val_max] = val_max 
    return data_adjusted

def rescale_ct(all_cases_folder="/MRIData/WuHuKidney/OtherCentersData/ZhongLiu/TouMingXiBaoLiu_nii"):
    '''
    all_cases_folder: contains all cases.
    '''
    # 设置包含多个子文件夹的父文件夹路径
    parent_folder = all_cases_folder
    # 循环遍历每个子文件夹
    for subdir in tqdm(os.listdir(parent_folder)):
        subdir_path = os.path.join(parent_folder, subdir)
        
        # 确保是文件夹
        if os.path.isdir(subdir_path):
            # 初始化子文件夹内的.nii.gz文件列表
            for file in os.listdir(subdir_path):
                if file.endswith('.nii.gz') and 'src' in file and 'rescaled' not in file:
                    img = sitk.ReadImage(os.path.join(subdir_path, file))
                    data = sitk.GetArrayFromImage(img)
                    data=adjust_ww_wl(data)
                    data = (data-data.min())/(data.max()-data.min())
                    rescaled_img = sitk.GetImageFromArray(data)
                    rescaled_img.CopyInformation(img)
                    sitk.WriteImage(rescaled_img, os.path.join(subdir_path,f'rescaled_{file}'))

if __name__=="__main__":
    rescale_ct(all_cases_folder="/homes/xchang/Data/WuHuKidney/nii_data/ZhongLiu/XianSeXiBaoLiu_nii")