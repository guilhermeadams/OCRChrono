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
9. The regex pattern (r"\d{1,2} de [a-zA-Z]+ de \d{4}") matches dates in the format of "Day de Month de Year", e.g. "1 de Janeiro de 2022" in Portuguese. The regex pattern searches for a sequence of one or two digits followed by the word "de", then one or more alphabetical characters for the month, followed again by "de" and finally four digits for the year.
10. This regex pattern is used in the OCR-based image sorter app to extract dates from OCR text in images that contain dates in this specific format. The extracted date string is then parsed into a Python datetime object using the dateparser library.

Here are ten regex patterns for date extraction:

```python
import re

# Matches dates in the format "MM/DD/YYYY" or "M/D/YYYY"
pattern1 = re.compile(r"\d{1,2}\/\d{1,2}\/\d{4}")

# Matches dates in the format "MM-DD-YYYY" or "M-D-YYYY"
pattern2 = re.compile(r"\d{1,2}-\d{1,2}-\d{4}")

# Matches dates in the format "YYYY/MM/DD" or "YYYY/M/D"
pattern3 = re.compile(r"\d{4}\/\d{1,2}\/\d{1,2}")

# Matches dates in the format "Month Day, Year", e.g. "January 1, 2022"
pattern4 = re.compile(r"[A-Za-z]+\s\d{1,2},\s\d{4}")

# Matches dates in the format "Day Month Year", e.g. "1 January 2022"
pattern5 = re.compile(r"\d{1,2}\s[A-Za-z]+\s\d{4}")

# Matches dates in the format "Day Month 'Year", e.g. "1 January '22"
pattern6 = re.compile(r"\d{1,2}\s[A-Za-z]+\s'\d{2}")

# Matches dates in the format "DD.MM.YY" or "DD.MM.YYYY"
pattern7 = re.compile(r"\d{1,2}\.\d{1,2}\.\d{2,4}")

# Matches dates in the format "Month Day 'Year", e.g. "January 1 '22"
pattern8 = re.compile(r"[A-Za-z]+\s\d{1,2}\s'\d{2}")

# Matches dates in the format "YYYY-MM-DD" or "YYYY-M-D"
pattern9 = re.compile(r"\d{4}\-\d{1,2}\-\d{1,2}")

# Matches dates in the format "Day Month Year", e.g. "1 January 2022"
pattern10 = re.compile(r"\d{1,2}\s[A-Za-z]+\s\d{2,4}")


## Disclaimer :warning:

This script is intended for educational purposes only :books:. The accuracy of the date extraction from OCR may not be reliable and may require further testing before use in a production environment. :exclamation:
