# 📄 pdf-ocr-docx

Convert scanned PDFs to editable Word documents using Tesseract OCR.

A lightweight Python tool that turns PDF pages into images, extracts text via OCR (Tesseract), and exports it to a `.docx` file. Supports **English** and **Farsi** by default, and can be extended to any Tesseract-supported language.

---

## ⚙️ Prerequisites

### ✅ Install Tesseract

Before running this tool, you **must install Tesseract OCR** from the following link:

👉 [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)

> ⚠️ **Important:**  
> Do **not change the default installation path** (`C:\Program Files\Tesseract-OCR`) during setup.  
> If you install it in a custom location, update the path in the Python code:

```python
pytesseract.pytesseract.tesseract_cmd = r'YOUR\CUSTOM\PATH\tesseract.exe'
