# for file in *.nii; do mv "$file" "MiBirth0067_$file"; done // file rename 
# gzip -k  *.nii  // .nii to .nii.gz compression   
# gunzip -k *.nii.gz //unzip .nii.gz to .nii


# Command+K+C   Command+K+U


#file name replace labelTr
# cd /Users/bhautikposhiya/ThesProj/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task001_MyTask/labelsTr

# nii_counter=1
# niigz_counter=1

# for file in $(ls -v *.nii*); do
#   if [[ $file == *.nii.gz ]]; then
#     formatted_counter=$(printf "%04d" "$niigz_counter")
#     new_name="VesselDetection_${formatted_counter}.nii.gz"
#     mv "$file" "$new_name"
#     ((niigz_counter++))
#   else
#     formatted_counter=$(printf "%04d" "$nii_counter")
#     new_name="VesselDetection_${formatted_counter}.nii"
#     mv "$file" "$new_name"
#     ((nii_counter++))
#   fi
# done



# file name replace for ImageTr
# cd /Users/bhautikposhiya/ThesProj/nnUNet/nnUNet_raw_data_base/nnUNet_raw_data/Task001_MyTask/imagesTr

# nii_counter=1
# niigz_counter=1

# for file in $(ls -v *.nii*); do
#   if [[ $file == *.nii.gz ]]; then
#     formatted_counter=$(printf "%04d" "$niigz_counter")
#     new_name="VesselDetection_${formatted_counter}_0000.nii.gz"
#     mv "$file" "$new_name"
#     ((niigz_counter++))
#   else
#     formatted_counter=$(printf "%04d" "$nii_counter")
#     new_name="VesselDetection_${formatted_counter}_0000.nii"
#     mv "$file" "$new_name"
#     ((nii_counter++))
#   fi
# done


