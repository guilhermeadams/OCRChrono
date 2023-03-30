# Image Sorter :camera:

This script searches for image files (.jpg, .jpeg, .png, .bmp, .tiff) in the same directory as the script and its subdirectories, and sorts them based on the date found in the image's OCR (Optical Character Recognition) result :mag_right:.

## Prerequisites :page_with_curl:

This script requires the following packages to be installed:
- easyocr :mag:
- dateparser :calendar:

You can install them via pip:

pip install easyocr dateparser

## Usage :computer:

Simply run the script:

python image_sorter.py

The script will search for image files in the same directory as the script and its subdirectories, extract the date from each image's OCR result, and rename each image file in ascending order based on its creation date.

## How it works :wrench:

1. The script creates an EasyOCR reader for the Portuguese language.
2. It searches for image files in the same directory as the script and its subdirectories, and stores their paths in a list.
3. For each image file, the script extracts the text from the image using EasyOCR.
4. It then searches for a date pattern in the extracted text using a regular expression.
5. If a date is found, it converts the date string to a datetime object using dateparser.
6. It stores the image path and its corresponding creation date in a dictionary.
7. The dictionary is sorted by creation date in ascending order.
8. Each image file is renamed in ascending order based on its creation date.

## Disclaimer :warning:

This script is intended for educational purposes only :books:. The accuracy of the date extraction from OCR may not be reliable and may require further testing before use in a production environment. :exclamation:
