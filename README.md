# OCR Image Processing using Pytesseract
=====================================

This Python script uses the Pytesseract library to perform Optical Character Recognition (OCR) on an image file. The script is designed to work with the Tesseract OCR engine, which is widely used for extracting text from images.

## Installation

To use this script, you'll need to have the following packages installed:

* Pytesseract
* Pillow (for image processing)

You can install these packages using pip:
```
pip install pytesseract pillow
```
## Usage

The script takes a single argument, the path to an image file. For example:
```
python ocr.py img.jpg
```
This will run the OCR process on the `img.jpg` file and print the extracted text to the console.

## Configuration

The script sets the following environment variables to configure the Tesseract OCR engine:

* `TESSDATA_PREFIX`: The path to the Tesseract data directory, which contains the necessary trained data for the OCR engine.
* `tesseract_cmd`: The path to the Tesseract command-line tool.

These settings are hardcoded in the script for now, but you can modify them if necessary.

## Exception Handling

The script catches any exceptions that may occur during the OCR process and prints an error message to the console.

## Contributing

Contributions are welcome! If you'd like to improve this script, please fork it and submit a pull request with your changes.

## License

This script is released under the MIT License. See the included LICENSE file for more information.
