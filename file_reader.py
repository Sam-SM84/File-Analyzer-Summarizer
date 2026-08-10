import pymupdf

def load_PDF(path):
    text = ""
    file = pymupdf.open(path)
    
    for page in file:
        text += page.get_text()
    return text , file

def load_text(path):
    file = open(path,'r')
    text = file.read()
    file.close()
    return text
