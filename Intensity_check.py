import os
import nibabel as nib
import numpy as np
import csv

# === Your paths ===
scan_dir = "/home/gpuadmin/Desktop/Bhautik_Poshiya/nnunet_bhautik/raw/Dataset001_VesselDetection/imagesTr/"
mask_dir = "/home/gpuadmin/Desktop/Bhautik_Poshiya/nnunet_bhautik/result/Dataset001_VesselDetection/nnUNetTrainer__nnUNetPlans__2d/fold_0/validation/"
output_csv = "/home/gpuadmin/Desktop/Bhautik_Poshiya/nnunet_bhautik/Visualizations/intensity_report.csv"

# === Write CSV ===
with open(output_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Filename", "Mean Inside", "Max Inside", "Mean Outside", "Slice"])

    for filename in os.listdir(scan_dir):
        if filename.endswith(".nii.gz"):
            # Remove "_0000" to match mask name
            case_id = filename.replace("_0000.nii.gz", "")
            scan_path = os.path.join(scan_dir, filename)
            mask_path = os.path.join(mask_dir, f"{case_id}.nii.gz")

            if not os.path.exists(mask_path):
                print(f"Skipping {filename} – mask not found.")
                continue

            try:
                scan = nib.load(scan_path).get_fdata()
                mask = nib.load(mask_path).get_fdata()

                # Analyze middle slice
                z = scan.shape[2] // 2
                scan_slice = scan[:, :, z]
                mask_slice = mask[:, :, z]

                inside = scan_slice[mask_slice > 0]
                outside = scan_slice[mask_slice == 0]

                writer.writerow([
                    case_id,
                    round(float(np.mean(inside)), 2) if inside.size > 0 else 0,
                    round(float(np.max(inside)), 2) if inside.size > 0 else 0,
                    round(float(np.mean(outside)), 2) if outside.size > 0 else 0,
                    z
                ])

                print(f"✅ Processed {case_id}")
            except Exception as e:
                print(f"⚠️ Error with {case_id}: {e}")

print(f"\n✅ All done! Report saved to:\n{output_csv}")
