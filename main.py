#!/usr/bin/env python3

'''
Created on Nov 11, 2021

@author: larissa

@brief: Very simple usage example

@var input(str): Expects a file or a folder.
'''

from PdfGenerator import PDFCreator

txt_file = "/home/larissa/TestFiles/Zen.txt"
csv_file = "/home/larissa/TestFiles/Zen.csv"
docx_file = "/home/larissa/TestFiles/Zen.docx"
odt_file = "/home/larissa/TestFiles/Zen.odt"
dir = "/home/larissa/TestFiles"
logo_png = "/home/larissa/TestFiles/Python-logo.png"
logo_jpg = "/home/larissa/TestFiles/Python-logo.jpg"

make_pdf = PDFCreator(dir)  