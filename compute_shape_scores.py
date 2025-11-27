import os
import nibabel as nib
import numpy as np
import pandas as pd
from skimage.measure import label, regionprops

label_dir = "/Users/bhautikposhiya/ThesProj/Bhautik_Poshiya/nnunet_bhautik/raw/Dataset001_VesselDetection/labelsTr"
output_csv = "vessel_shape_scores.csv"
results = []

for file in os.listdir(label_dir):
    if file.endswith(".nii.gz"):
        filepath = os.path.join(label_dir, file)
        nii = nib.load(filepath)
        mask = nii.get_fdata()
        shape_scores = []

        for i in range(mask.shape[2]):
            slice_mask = mask[:, :, i]
            if np.any(slice_mask):
                labeled = label(slice_mask)
                regions = regionprops(labeled)
                for region in regions:
                    if region.major_axis_length > 0:
                        roundness = region.minor_axis_length / region.major_axis_length
                        shape_scores.append(min(roundness, 1.0))

        avg_score = np.mean(shape_scores) if shape_scores else 0
        results.append({"filename": file, "mean_shape_score": round(avg_score, 3)})

df = pd.DataFrame(results)
df.to_csv(output_csv, index=False)
print(f"Saved: {output_csv}")