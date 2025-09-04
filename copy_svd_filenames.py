#!/usr/bin/env python3
"""
Script to copy filenames from svd_orig directory to a new file.
This script recursively walks through the svd_orig directory and writes
all filenames (including those in subdirectories) to svd_filenames.txt
"""

import os
import sys
from pathlib import Path

def copy_svd_filenames():
    """
    Walk through svd_orig directory and write all filenames to svd_filenames.txt
    """
    svd_orig_path = Path("svd_orig")
    output_file = "svd_filenames.txt"
    
    # Check if svd_orig directory exists
    if not svd_orig_path.exists():
        print(f"Error: Directory '{svd_orig_path}' does not exist!")
        sys.exit(1)
    
    if not svd_orig_path.is_dir():
        print(f"Error: '{svd_orig_path}' is not a directory!")
        sys.exit(1)
    
    filenames = []
    
    # Walk through the directory recursively
    for root, dirs, files in os.walk(svd_orig_path):
        for file in files:
            # Get the full path of the file
            file_path = Path(root) / file
            # Get the relative path from svd_orig
            relative_path = file_path.relative_to(svd_orig_path)
            filenames.append(str(relative_path))
    
    # Sort filenames for consistent output
    filenames.sort()
    
    # Write filenames to output file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for filename in filenames:
                f.write(f"{filename}\n")
        
        print(f"Successfully wrote {len(filenames)} filenames to '{output_file}'")
        print(f"Files found in: {svd_orig_path}")
        
    except Exception as e:
        print(f"Error writing to '{output_file}': {e}")
        sys.exit(1)

if __name__ == "__main__":
    copy_svd_filenames() 