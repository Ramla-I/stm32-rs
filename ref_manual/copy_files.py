import os
import shutil
import xml.etree.ElementTree as ET
import argparse

# Paths to source directories
REF_MANUAL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))
SVD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'svd'))
XML_PATH = os.path.join(REF_MANUAL_DIR, 'rm_device_mapping.xml')

parser = argparse.ArgumentParser(description='Copy reference manual PDFs and SVD files into folders.')
parser.add_argument('dest_dir', help='Destination directory for output folders')
args = parser.parse_args()

def warn(msg):
    print(f"WARNING: {msg}")

def main():
    tree = ET.parse(XML_PATH)
    root = tree.getroot()

    for rm in root.findall('reference_manual'):
        rm_name = rm.get('rm')  # e.g., 'RM0360'
        if not rm_name:
            continue
        folder_path = os.path.join(args.dest_dir, rm_name.lower())
        if os.path.exists(folder_path):
            continue  # Skip if folder already exists
        os.makedirs(folder_path, exist_ok=True)

        # Copy PDF
        pdf_name = f"{rm_name.lower()}.pdf"
        pdf_src = os.path.join(REF_MANUAL_DIR, pdf_name)
        pdf_dst = os.path.join(folder_path, pdf_name)
        if os.path.exists(pdf_src):
            shutil.copy2(pdf_src, pdf_dst)
        else:
            warn(f"PDF not found: {pdf_src}")

        # Copy SVD files
        svd_elem = rm.find('svd')
        if svd_elem is not None:
            for svd_file_elem in svd_elem.findall('svd_file'):
                svd_name = svd_file_elem.text.strip()
                svd_src = os.path.join(SVD_DIR, svd_name)
                svd_dst = os.path.join(folder_path, svd_name)
                if os.path.exists(svd_src):
                    shutil.copy2(svd_src, svd_dst)
                else:
                    warn(f"SVD not found: {svd_src}")

if __name__ == '__main__':
    main()
