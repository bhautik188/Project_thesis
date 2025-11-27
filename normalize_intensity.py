import os
import nibabel as nib
import numpy as np
import pandas as pd

# Input and output folders
input_dir = "/home/gpuadmin/Desktop/Bhautik_Poshiya/nnunet_bhautik/raw/Dataset001_VesselDetection/imagesTr/"
output_dir = "/home/gpuadmin/Desktop/Bhautik_Poshiya/nnunet_bhautik/raw/Dataset001_VesselDetection/imagesTr_scaled_intensity_masked/"
csv_path = "/home/gpuadmin/Desktop/Bhautik_Poshiya/nnunet_bhautik/Visualizations/intensity_report.csv"

# Intensity clipping and scaling
clip_min = 40
clip_max = 150
scale_max = 2.0

# Create output directory if it does not exist
os.makedirs(output_dir, exist_ok=True)

# Load intensity report and select valid scans
df = pd.read_csv(csv_path)
valid_cases = df[df["Mean Inside"] > 0]["Filename"].tolist()

for case_id in valid_cases:
    filename = f"{case_id}_0000.nii.gz"
    input_path = os.path.join(input_dir, filename)
    output_path = os.path.join(output_dir, filename)

    if not os.path.exists(input_path):
        print(f"Skipping missing file: {filename}")
        continue

    print(f"Normalizing: {filename}")
    image = nib.load(input_path)
    data = image.get_fdata()

    # Clip and scale
    clipped = np.clip(data, clip_min, clip_max)
    normalized = (clipped - clip_min) / (clip_max - clip_min) * scale_max

    # Save normalized image
    normalized_img = nib.Nifti1Image(normalized, affine=image.affine, header=image.header)
    nib.save(normalized_img, output_path)

print("All valid scans have been normalized and saved.")
