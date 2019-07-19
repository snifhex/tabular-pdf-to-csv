"""
Tabular data from pdf extractor.
This script will automatically analyse all the pdf files from the folder and will check for tables in them and 
then automatically create output folder in which there will the folder with the name of pdf and under that folder 
there will be csv's and json files of the tables from that pdf
"""

import os
import camelot
from PyPDF2 import PdfFileReader


def create_folder(file_name):
    """Will create output folder if it doesn't exist output folder will
        be created and inside that a new folder will be created acording
        to the pdf file name"""

    if os.path.exists('output'):
        os.mkdir(f'output/{file_name}')
    else:
        os.mkdir('output')
        os.mkdir(f'output/{file_name}')
        
def total_pages(pdf):
    """Will find out total number of pages in given pdf and will return string of all the page numbers."""
    
    pdf_object = PdfFileReader(open(pdf, 'rb'))
    pages = ','.join([str(i) for i in list(range(pdf_object.getNumPages()))])
    return pages

def main():
    """Main Function which is responsible for pdf parsing and exporting it into csv."""
    
    for pdf in os.listdir():
        file_name, file_extension = os.path.splitext(pdf)
        if file_extension == '.pdf':
            print(pdf)
            # Change this pages variable according to your pdf if you don't want to parse all the pages. 
            pages = total_pages(pdf)
            #Remove flavor parameter if you want to parse pdf's without visible borders.
            tables = camelot.read_pdf(
                pdf, flavor='stream', pages=pages, )
            create_folder(file_name)
            tables.export(f'./output/{file_name}tables.csv', f='csv')


if __name__ == "__main__":
    main()
