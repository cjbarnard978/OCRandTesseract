import os
import sys
from pathlib import Path
import argparse
from pdf2image import convert_from_path

required_packages = ['numpy', 'pandas', 'pytesseract', 'Pillow', 'opencv-python', 'pdf2image']
missing = []

import os
import sys
from pathlib import Path
import argparse
from pdf2image import convert_from_path

required_packages = ['numpy', 'pandas', 'pytesseract', 'Pillow', 'opencv-python', 'pdf2image']
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

pdf_dir = Path('/Users/ceciliabarnard/Desktop//8510/ocrtesseract/ocrai/pdf')

output_dir = Path('/Users/ceciliabarnard/Desktop/8510/ocrtesseract/ocrai/pdf/converted_images')
output_dir.mkdir(exist_ok=True)

for pdf_path in pdf_dir.glob('*.pdf'):
    try:
        print(f'Processing: {pdf_path.name}')
        images = convert_from_path(pdf_path, output_folder=output_dir, fmt='png')
        print(f'  Converted {len(images)} pages from {pdf_path.name}')
    except Exception as e:
        print(f'  ❌ Error processing {pdf_path.name}: {e}')

quality_settings = {
            'high': {'dpi': 300, 'format': 'PNG'},
            'medium': {'dpi': 200, 'format': 'PNG'},
            'low': {'dpi': 150, 'format': 'JPEG'}
        }
settings = quality_settings.get('high', quality_settings['high'])

def ocr_conversion(image_path, lang='lat'):
    print('running ocr')
    text, data = run_ocr_psm3(image_path, lang=lang)
    
    if text and data:
        confidence = analyze_text_confidence(data)
        cleaned_text = clean_text(text) 
        result = {
            'text': cleaned_text,
            'confidence': confidence,
            'word count': word_count
        }
        print(print(f"Words extracted: {word_count}"))
        input_dir = Path('/Users/ceciliabarnard/Desktop/8510/ocrtesseract/ocrai/pdf/grayscale_images')
        low_conf_dir = Path('/Users/ceciliabarnard/Desktop/8510/ocrtesseract/ocrai/pdf/low confidence')
        low_conf_dir.mkdir(exist_ok=True)
        
        for img_path in input_dir.glob('*.png'):
            image = Image.open(img_path)
            data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
            confidences = [int(conf) for conf in data['conf'] if conf.isdigit() and int(conf) > 0]
            mean_conf = sum(confidences) / len(confidences) if confidences else 0
            text = pytesseract.image_to_string(image)
            if mean_conf < 60:
                out_file = low_conf_dir / (img_path.stem + '_low_conf.txt')
                with open(out_file, 'w', encoding='utf-8') as f:
                    f.write(text)
                print(f'Saved low confidence text from {img_path.name} (mean confidence: {mean_conf:.1f})')
            else:
                print(f'{img_path.name} passed with mean confidence: {mean_conf:.1f}')                from pathlib import Path
                from PIL import Image
                import pytesseract
                
                input_dir = Path('/Users/ceciliabarnard/Desktop/8510/ocrtesseract/ocrai/pdf/grayscale_images')
                low_conf_dir = Path('/Users/ceciliabarnard/Desktop/8510/ocrtesseract/ocrai/pdf/low confidence')
                low_conf_dir.mkdir(exist_ok=True)
                
                for img_path in input_dir.glob('*.png'):
                    image = Image.open(img_path)
                    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
                    confidences = [int(conf) for conf in data['conf'] if conf.isdigit() and int(conf) > 0]
                    mean_conf = sum(confidences) / len(confidences) if confidences else 0
                    text = pytesseract.image_to_string(image)
                    if mean_conf < 60:
                        out_file = low_conf_dir / (img_path.stem + '_low_conf.txt')
                        with open(out_file, 'w', encoding='utf-8') as f:
                            f.write(text)
                        print(f'Saved low confidence text from {img_path.name} (mean confidence: {mean_conf:.1f})')
                    else:
                        print(f'{img_path.name} passed with mean confidence: {mean_conf:.1f}')rd/Desktop/8510/ocrtesseract/ocrai/pdf/low confidence')
low_conf_dir.mkdir(exist_ok=True)

for img_path in grayscale_dir.glob('*.png'):
    image = Image.open(img_path)
    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
    confidences = [int(conf) for conf in data['conf'] if conf.isdigit() and int(conf) > 0]
    mean_conf = sum(confidences) / len(confidences) if confidences else 0
    text = pytesseract.image_to_string(image)
    if mean_conf < 60:
        out_file = low_conf_dir / (img_path.stem + '_low_conf.txt')
        with open(out_file, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f'Saved low confidence text from {img_path.name} (mean confidence: {mean_conf:.1f})')
    else:
        print(f'{img_path.name} passed with mean confidence: {mean_conf:.1f}')

def ocr_conversion(image_path, lang='lat'):
    print('running ocr')
    text, data = run_ocr_psm3(image_path, lang=lang)
    
    if text and data:
        confidence = analyze_text_confidence(data)
        cleaned_text = clean_text(text) 
        result = {
            'text': cleaned_text,
            'confidence': confidence,
            'word count': word_count
        }
        print(print(f"Words extracted: {word_count}"))
        

      
