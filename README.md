# ASCII Image Processing using NumPy

##  Overview

This project converts an input image into:

* Grayscale image
* Negative image
* ASCII art (text-based image)

It demonstrates how images can be represented as numerical arrays and transformed using NumPy.

---

##  Concept

* An image is treated as a NumPy array
* RGB values are averaged to create grayscale
* Pixel values are inverted for negative image
* Brightness values are mapped to characters to generate ASCII art

---

## ⚙️ Requirements

* Python 3
* NumPy
* Pillow

Install dependencies:
pip install numpy pillow

---

##  How to Run

1. Place your image as `new.jpeg` in the project folder
2. Run the script:

python project.py

---

##  Output Files

* `gray.jpeg` → Grayscale image
* `neg.jpeg` → Negative image
* `ascii_art.txt` → ASCII representation

---

## Example Idea

Dark pixels are represented by dense characters like `@`
Light pixels are represented by spaces or `.`

---

##  Future Improvements

* Colored ASCII output
* GUI interface
* Real-time image processing

---

## 👤 Author

Aakash Singh
