import os
import nibabel as nib
from tqdm import tqdm

# 定义保存信息的.txt文件路径
output_file = 'data_info.txt'

# 定义包含数据的文件夹路径
data_folder = '/MRIData/WuHuKidney/OtherCentersData/ZhongLiu/TouMingXiBaoLiu_nii'

# 打开.txt文件以写入模式
with open(output_file, 'w') as file:
    # 获取数据文件夹中的所有子文件夹
    subfolders = sorted([f.path for f in os.scandir(data_folder) if f.is_dir()])

    # 遍历每个子文件夹
    for subfolder in tqdm(subfolders):
        subfolder_name = os.path.basename(subfolder)
        file.write(f"子文件夹名称: {subfolder_name}\n")

        # 获取子文件夹中的所有.nii.gz文件
        nii_files = [f.name for f in os.scandir(subfolder) if f.name.endswith('.nii.gz')]

        # 遍历每个.nii.gz文件
        for nii_file in nii_files:
            file_path = os.path.join(subfolder, nii_file)

            # 读取.nii.gz文件
            img = nib.load(file_path)

            # 获取数据数组
            data = img.get_fdata()

            # 计算分辨率和强度范围
            resolution = img.header.get_zooms()
            intensity_range = (data.min(), data.max())

            file.write(f"  文件名称: {nii_file}\n")
            file.write(f"  分辨率: {resolution}\n")
            file.write(f"  强度范围: {intensity_range}\n\n")
