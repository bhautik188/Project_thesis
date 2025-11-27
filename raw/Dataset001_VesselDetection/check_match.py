import os
import re

# Define paths for the images and labels folders
images_folder = '/Users/bhautikposhiya/ThesProj/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task001_MyTask/imagesTr'
labels_folder = '/Users/bhautikposhiya/ThesProj/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task001_MyTask/labelsTr'

# Print folder paths to verify
print("Images folder path:", images_folder)
print("Labels folder path:", labels_folder)

# Get sorted lists of image and label files with either .nii or .nii.gz extensions
image_files = sorted(f for f in os.listdir(images_folder) if f.endswith('.nii.gz'))
label_files = sorted([f for f in os.listdir(labels_folder) if f.endswith('.nii.gz')])

# Print found files for debugging
print("Image files found:", image_files)
print("Label files found:", label_files)

# Regular expression to match the file naming pattern
image_pattern = re.compile(r'^(MiBirth\d+_s\d+a\d+)(\.nii|\.nii.gz)$')
label_pattern = re.compile(r'^(MiBirth\d+_s\d+a\d+)_seg(\.nii|\.nii.gz)$')

# Initialize counter for matched pairs
counter = 1

# Loop through each image file and find the matching label file
for image_file in image_files:
    image_match = image_pattern.match(image_file)
    if not image_match:
        print(f"No match for image file: {image_file}")
        continue

    # Extract the base name for image (without extension)
    base_name = image_match.group(1)
    
    # Construct the expected label file name
    label_file = f"{base_name}_seg{image_match.group(2)}"  # Keeps same extension (.nii or .nii.gz)
    
    if label_file in label_files:
        # Print matched names for verification
        print(f"Match {counter}:")
        print(f"Image: {image_file}")
        print(f"Label: {label_file}")
        print("--------")
        
        # Increment the counter for the next pair
        counter += 1
    else:
        print(f"No matching label file found for {image_file}")