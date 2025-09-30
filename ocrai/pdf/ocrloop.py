import os
import sys
from pathlib import Path
import argparse

required_packages = ['numpy', 'pandas', 'pytesseract', 'Pillow', 'opencv-python']
missing = []

for pkg in required_packages:
    try:
        if pkg == 'Pillow':
            import PIL
        elif pkg == 'opencv-python':
            import cv2
        else:
            __import__(pkg)
    except ImportError:
        missing.append(pkg)

if missing: 
    print("missing packages")
    import subprocess 
    subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing)

pdf_dir = Path('/8510/ocrtesseract/ocrai/pdf')

for pdf in Path.glob(pdf_dir, '*.pdf'):
    from pdf2image import convert_from_path, convert_from_bytes 
    from pdf2image.exceptions import ( 
    PDFInfoNotInstalledError, 
    PDFPageCountError, 
    PDFSyntaxError 
) 
print('pdf')
   
output_dir = Path('/8510/ocrtesseract/ocrai/pdf/converted_images')
output_dir.mkdir(exist_ok=True)
images_from_path = convert_from_path(pdf_path, output_folder=output_dir, fmt='png')

  
