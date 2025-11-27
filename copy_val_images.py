import json
import shutil
import os

split_file = "/home/gpuadmin/Desktop/Bhautik_Poshiya/nnunet_bhautik/preprocessing/Dataset001_VesselDetection/splits_final.json"
images_tr = "/home/gpuadmin/Desktop/Bhautik_Poshiya/nnunet_bhautik/raw/Dataset001_VesselDetection/imagesTr"
val_images_out = "/home/gpuadmin/Desktop/Bhautik_Poshiya/nnunet_bhautik/raw/Dataset001_VesselDetection/val_images"

os.makedirs(val_images_out, exist_ok=True)

with open(split_file, 'r') as f:
    splits = json.load(f)

val_cases = splits[0]['val']  # fold 0

for case in val_cases:
    name = case + "_0000.nii.gz"
    src = os.path.join(images_tr, name)
    dst = os.path.join(val_images_out, name)
    if os.path.exists(src):
        shutil.copy(src, dst)
        print(f"✅ Copied {name}")
    else:
        print(f"❌ Missing: {name}")
