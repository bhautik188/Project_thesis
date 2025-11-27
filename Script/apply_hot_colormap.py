import os
import nibabel as nib
import numpy as np
import cv2

# Set input and output directories
nii_folder = '/home/gpuadmin/Desktop/Bhautik_Poshiya/nnunet_bhautik/raw/Dataset001_VesselDetection/imagesTr/'
output_folder = '/home/gpuadmin/Desktop/Bhautik_Poshiya/nnunet_bhautik/Visualizations/hot_colormaps/'

# Create output directory if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# List all .nii.gz files
nii_files = [f for f in os.listdir(nii_folder) if f.endswith('.nii.gz')]

print(f"Found {len(nii_files)} files in imagesTr folder")

# Process each .nii.gz file
for file in nii_files:
    print(f"\nProcessing {file}")
    path = os.path.join(nii_folder, file)
    img = nib.load(path)
    data = img.get_fdata()

    print(f"Shape: {data.shape}")
    
    # Decide which slices to extract
    if data.ndim == 3 and data.shape[2] > 1:
        z_center = data.shape[2] // 2
        slice_indices = [z_center - 1, z_center, z_center + 1]
    else:
        slice_indices = [0]

    for idx in slice_indices:
        if idx < 0 or idx >= data.shape[2]:
            continue
        
        slice_data = data[:, :, idx]

        # Normalize safely
        if np.max(slice_data) == np.min(slice_data):
            print(f"Slice {idx} is flat. Skipping.")
            continue

        norm_slice = (slice_data - np.min(slice_data)) / (np.max(slice_data) - np.min(slice_data))
        slice_uint8 = (norm_slice * 255).astype(np.uint8)

        # Apply hot colormap
        hot_image = cv2.applyColorMap(slice_uint8, cv2.COLORMAP_HOT)

        # Generate output name and save
        base = file.replace('.nii.gz', '')
        out_name = f"{base}_slice{idx}.png"
        out_path = os.path.join(output_folder, out_name)
        cv2.imwrite(out_path, hot_image)
        print(f"Saved: {out_path}")

print("\nDone converting all .nii.gz files to hot colormap PNGs.")
