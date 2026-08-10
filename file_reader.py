import pymupdf

def loadPDF(path):
    text = ""
    file = pymupdf.open(path)
    
    for page in file:
        text += page.get_text()
    return text , file