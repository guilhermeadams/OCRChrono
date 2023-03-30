import os
import re
from glob import glob
from pathlib import Path

import dateparser
import easyocr

# Create an EasyOCR reader
reader = easyocr.Reader(['pt'])

# Regex pattern for date extraction
date_pattern = re.compile(r"\d{1,2} de [a-zA-Z]+ de \d{4}")


def find_images(path):
    # Search for image files recursively
    image_extensions = ["*.jpg", "*.jpeg", "*.png", "*.bmp", "*.tiff"]
    image_files = []
    for ext in image_extensions:
        image_files.extend(glob(os.path.join(path, "**", ext), recursive=True))
    return image_files


def extract_date(image_path):
    # OCR with EasyOCR
    ocr_result = reader.readtext(image_path, detail=0)

    # Find date in OCR result
    ocr_text = " ".join(ocr_result)
    date_match = date_pattern.search(ocr_text)

    # Return datetime object if date is found, else None
    if date_match:
        date_str = date_match.group(0)
        date_obj = dateparser.parse(date_str, languages=['pt'])
        return date_obj
    return None


def main():
    script_path = os.path.dirname(os.path.realpath(__file__))
    image_files = find_images(script_path)

    # Extract creation dates and store in a dictionary
    image_dates = {}
    for image_path in image_files:
        date_obj = extract_date(image_path)
        if date_obj:
            image_dates[image_path] = date_obj

    # Print image_dates for debugging
    print("image_dates:")
    print(image_dates)

    # Sort images by creation date
    sorted_images = sorted(image_dates.items(), key=lambda x: x[1])

    # Rename image files
    for i, (image_path, date_obj) in enumerate(sorted_images, 1):
        new_path = os.path.join(os.path.dirname(image_path), f"{i}.{Path(image_path).suffix}")
        os.rename(image_path, new_path)


if __name__ == "__main__":
    main()
