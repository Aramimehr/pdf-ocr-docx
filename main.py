from pdf2image import convert_from_path
from typing import List,AnyStr, Optional
import pytesseract
from PIL import Image
from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from enum import Enum
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class PDFImageConverter:
    
    def __init__(self,pdf_path: str, first_page:int = 1, last_page = None):
        self.pdf_path: str = pdf_path
        self.first_page = first_page
        self.last_page = last_page
        self._images: Optional[List] = None



    
    def _load_images(self):
        if self._images is None:
            print("Converting PDF to images... Please wait.")
            if self.last_page is not None:
                self._images = convert_from_path(self.pdf_path,first_page=self.first_page,last_page=self.last_page)
            else:
                self._images = convert_from_path(self.pdf_path,first_page=self.first_page)
                
    
    def save_page_as_image(self, page_num: int = 1, output_name: Optional[AnyStr] = None):
        output_name = f"page_{page_num}.png"
        self._load_images()
        self._images[page_num - 1].save(output_name, "PNG")
        print(f"Page {page_num} saved as {output_name}")
        return output_name
        
        
class ExtractText:
    
    def __init__(self,image_name: str):
        self.image = image_name
        self.texts: Optional[List] = []
        
    def extract(self,language):
        img = Image.open(self.image)
        text = pytesseract.image_to_string(img, lang=language)
        self.texts.append(text)
        return text
        
        
        
class Doc:
    
    def __init__(self,doc_name):
        
        self.document_name = doc_name + '.docx'
        self.document = Document()
        
    def creat_document(self,text):
        
        paragraph = self.document.add_paragraph(text)
        paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT
        self.document.add_page_break()
        self.document.save(self.document_name)
        
        

class Language(Enum):
    eng = 1
    fas = 2

if __name__ == '__main__':
    pdf_path = input("PDF path:\n>> ")
    lang = int(input("Language:\n1-English\n2-Farsi\n>> "))
    first_page = int(input("Extract text from page ?\n>> "))
    last_page = int(input("to page ?\n>> "))
    document_name = input("output name:\n>> ")
         
    
    images = PDFImageConverter(pdf_path,first_page,last_page)
    myDoc = Doc(document_name)
    
    number_of_page = last_page - first_page + 1
    
    for i in range(first_page,number_of_page):
        image_name = images.save_page_as_image(i)
        image2txt = ExtractText(image_name)
        txt = image2txt.extract(Language(lang).name)
        myDoc.creat_document(txt)
        os.remove(image_name)
