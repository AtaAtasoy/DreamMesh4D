#!/bin/bash

# Directory containing the input subdirectories
input_dir="input"

# Iterate over all subdirectories in the input directory except "meshes"
for mesh_name in $(ls -d ${input_dir}/*/ | grep -v "${input_dir}/meshes/"); do
    # Remove the trailing slash from the subdirectory name
    mesh_name=$(basename "$mesh_name")
    
    # Run the command for each subdirectory
    python launch.py --train --config custom/threestudio-dreammesh4d/configs/sugar_static_refine.yaml data.mesh_name="$mesh_name"
done
