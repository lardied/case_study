#!/usr/bin/env python3

'''
Created on Nov 11, 2021

@author: larissa

@brief: This files reads given files and creates a pdf file depending which format is given. 

@var input(str): Expects a file or a folder.
'''

#system imports
import os
import sys
from fpdf import FPDF
from PIL import Image
import docx
from odf import text, teletype
from odf.opendocument import load


class PDFCreator():

    def __init__(self, input: str):
        #Check if a single file is given.
        if os.path.isfile(input):
            self.input_file = input
            self.input_path = "\\".join(self.input_file.split("\\")[0:-1])
            self.input_format = self.get_input_format()
            self.input_content = self.get_input_content()
            
            self.create_pdf_file()

        #Creates the new files in a loop, if a directory is given(handels multiple files).
        if os.path.isdir(input):
            for file in os.listdir(input):
                self.input_file = os.path.join(input, file)
                self.input_path = input
                self.input_format = self.get_input_format()
                self.input_content = self.get_input_content()
                    
                self.create_pdf_file()


    def get_input_format(self):
        #Get the file extension
        __, extension = os.path.splitext(self.input_file)
        return extension
    
    def get_input_content(self):
        content = str()
        #Check if the given format are supoorted.
        if self.input_format in (".txt", ".csv", ".docx", ".odt", ".png", ".jpg", "jpeg"):
            #Handles graphic files.
            if self.input_format in (".png", ".jpg", ".jpeg"):
                image = Image.open(self.input_file)
                content = image.convert("RGB")
            #Handles docx-files.
            elif self.input_format in (".docx"):
                doc = docx.Document(self.input_file)
                content = "\n".join(paragraph.text for paragraph in doc.paragraphs)
            #Handels odt-files.
            elif self.input_format in (".odt"):
                odt = load(self.input_file)
                lines = odt.getElementsByType(text.P)
                content = "".join((teletype.extractText(lines[i]) + "\n") for i in range(len(lines)))
            #Handels text-files.
            elif self.input_format in (".txt", ".csv"):
                with open(self.input_file, encoding="utf-8-sig") as f:
                    content = f.read()
                f.close()
    
            return content
    
        else: print("{} not supported/tested yet".format(self.input_format))

    def create_pdf_file(self):
        #check if there is content
        if self.input_content:
            #create the new filename 
            self.created_file = self.input_file.replace(".", "_") + str(".pdf")

            #if its a graphic file, use pillow to save the new file.
            if self.input_format in (".png", ".jpg", ".jpeg"):
                self.input_content.save(self.created_file)
            #if its a text file, use fpdf to save the new file.
            else:
                pdf = FPDF()
                pdf.add_page()
                pdf.set_xy(0, 0)
                pdf.set_font("arial", "B", 12.0)
                pdf.multi_cell(w=0, h=5, align="L", txt=self.input_content, border=0)
                pdf.output(self.created_file, "F")
            self.is_created()
        else: print("PDF has not been created.\n")

    def is_created(self):
        #simple check if the file is created.
        if os.path.isfile(self.created_file):
            print("PDF has been created.\n{}\n".format(self.created_file))
            
        
if __name__ == '__main__':
    PDFCreator(sys.argv[1])      



