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


from pathlib import Path
from PIL import Image

input_dir = Path('/Users/ceciliabarnard/Desktop/8510/ocrtesseract/ocrai/pdf/converted_images')
output_dir = Path('/Users/ceciliabarnard/Desktop/8510/ocrtesseract/ocrai/pdf/grayscale_images')
output_dir.mkdir(exist_ok=True)

for img_path in input_dir.glob('*.png'):
    with Image.open(img_path) as img:
        gray_img = img.convert('L')
        gray_img.save(output_dir / img_path.name)
        print(f'Converted {img_path.name} to grayscale.')

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
     else 
        print("FAILED") 
        return {}
def process_all_images(input_dir, lang='lat'): 
    total_words = 0
    successful_images = 0
    
import pytesseract 

input_dir = Path('/Users/ceciliabarnard/Desktop/8510/ocrtesseract/ocrai/pdf/grayscale_images')
results_dir = Path('/Users/ceciliabarnard/Desktop/8510/ocrtesseract/ocrai/pdf/results')
results_dir.mkdir(exist_ok=True)

for img_path in input_dir.glob('*.png'):
    try:
        image = Image.open(img_path)
        text = pytesseract.image_to_string(image, lang='lat')
        print(f'Processed {img_path.name}:')
        print(text[:200])
        print('-' * 40)
        # Calculate mean confidence
        data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
        confidences = [int(conf) for conf in data['conf'] if conf.isdigit() and int(conf) > 0]
        confidence = sum(confidences) / len(confidences) if confidences else 0
        # Save result to file
        result_file = results_dir / (img_path.stem + '.txt')
        with open(result_file, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f'Saved OCR result to {result_file}')
        # If confidence < 65, also save to low confidence file
        if confidence < 65:
            low_conf_file = results_dir / (img_path.stem + '_low_confidence.txt')
            with open(low_conf_file, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f'Low confidence ({confidence:.1f}%) result saved to {low_conf_file}')
    except Exception as e:
        print(f'❌ Error processing {img_path.name}: {e}')

import openai 
from openai import OpenAI 
openai.api_key = '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' 
def correct_text_with_openai(text): 
    response = openai.
'