import os
import shutil
import random

# Base directory
base_path = "/home/gpuadmin/Desktop/Bhautik_Poshiya/nnunet_bhautik/raw/Dataset001_VesselDetection"

# Source folders
image_tr_dir = os.path.join(base_path, "imagesTr")
label_tr_dir = os.path.join(base_path, "labelsTr")

# Target folders for test set
image_ts_dir = os.path.join(base_path, "imagesTs")
label_ts_dir = os.path.join(base_path, "labelsTs")

# Ensure target folders exist
os.makedirs(image_ts_dir, exist_ok=True)
os.makedirs(label_ts_dir, exist_ok=True)

# List all image files
all_image_files = [f for f in os.listdir(image_tr_dir) if f.endswith("_0000.nii.gz")]

# 80/20 split
num_total = len(all_image_files)
num_test = max(1, int(0.2 * num_total))
test_files = random.sample(all_image_files, num_test)

# Move files
for img_file in test_files:
    case_id = img_file.replace("_0000.nii.gz", "")
    label_file = f"{case_id}.nii.gz"

    # Move image and label to Ts folders
    shutil.move(os.path.join(image_tr_dir, img_file), os.path.join(image_ts_dir, img_file))
    shutil.move(os.path.join(label_tr_dir, label_file), os.path.join(label_ts_dir, label_file))

print(f"Moved {num_test} cases to testing set.")
