# OCR and AI correction with Tesseract and OpenAI

This script is a Python loop designed to provide OCR of historical documents. Using Tesseract OCR and OpenAI, it analyzes the confidence of each page of OCRed text and passes any with a confidence level of below 65% to OpenAI's gpt-3.5-turbo for correction. 
IMPORTANT: This script is not designed to analyze and OCR handwriting. It will only provide accurate results and run as intended if the PDFs included are typed. 

# Installing Tesseract 

On Mac: brew install tesseract on the command line

For more information and other operating systems consult tesseract-ocr.github.io/tessdoc/installation.html

To install other necessary packages see requirements.txt 

# How to Create and Activate a Virtual Environment 

Once in appropriate directory run python3 -m venv my_env in the terminal. 

to deploy: source my_env/bin/activate

# OpenAI API Key Instructions 

Create an OpenAI account using the email linked to the project.

Go to platform-openai.com/docs/quickstart/create-and-export-an-open-ai-key

Click the "Create an API Key" button. 

Make sure to copy and save your API key somewhere on your machine. If you forget your API key, delete the old one and generate a new one. 

IMPORTANT: DO NOT PUSH YOUR API KEY TO GITHUB. When pushing to github replace your secret API key with a placeholder-this script uses 'yourkeyhere' 

# How the Script Works 