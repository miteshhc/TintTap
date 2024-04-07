#!/bin/bash

folder_name="TintTap"

# Check if folder exists
if [ ! -d "$folder_name" ]; then
    # If the folder does not exists, then create it
    tar -xvf TintTap.tar.xz
fi

# Navigate into the folder
cd "$folder_name"

# Execute the binary
./TintTap
