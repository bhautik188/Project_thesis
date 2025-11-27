import os
import re
import numpy as np
import nibabel as nib
import cv2
from collections import defaultdict

# Set input/output paths
png_folder = '/home/gpuadmin/Desktop/Bhautik_Poshiya/nnunet_bhautik/Visualizations/hot_colormaps/'
output_folder = '/home/gpuadmin/Desktop/Bhautik_Poshiya/nnunet_bhautik/Visualizations/hot_nifti/'

# Create output folder if not exists
os.makedirs(output_folder, exist_ok=True)

# Group PNGs by base name
grouped_slices = defaultdict(dict)

for filename in os.listdir(png_folder):
    if filename.endswith('.png'):
        match = re.match(r'(.+)_slice(-?\d+)\.png', filename)
        if match:
            base_name, slice_idx = match.groups()
            grouped_slices[base_name][int(slice_idx)] = filename

# Convert each group into a .nii file
for base_name, slices in grouped_slices.items():
    print(f"Processing: {base_name}")

    # Sort slice indices and read images
    sorted_indices = sorted(slices.keys())
    slice_stack = []

    for idx in sorted_indices:
        img_path = os.path.join(png_folder, slices[idx])
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        slice_stack.append(img)

    # Stack slices into 3D volume
    volume = np.stack(slice_stack, axis=-1)

    # Create NIfTI and save
    nifti_img = nib.Nifti1Image(volume, affine=np.eye(4))
    out_path = os.path.join(output_folder, f'{base_name}.nii.gz')
    nib.save(nifti_img, out_path)

    print(f"Saved: {out_path}")

print("All PNG groups converted to .nii.gz successfully.")
