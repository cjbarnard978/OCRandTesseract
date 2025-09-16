import os 
import sys
from pathlib import Path 
import argparse 

def check_dependencies():
    """Check if required packages are installed."""
    required_packages = {
        'pdf2image': 'pdf2image',
        'PIL': 'Pillow',
        'cv2': 'opencv-python'
    }

    missing_packages = []

def convert_pdf_to_images(pdf_path, output_dir, dpi=300, quality='high', grayscale=True):