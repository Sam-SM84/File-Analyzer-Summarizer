import pymupdf

def load_PDF(arg):
    text = []
    if isinstance(arg,str):
        file = pymupdf.open(arg)

    else :
        text_file = arg.read()
        file = pymupdf.open(stream=text_file)
    
    for page in file:
        text.append(page.get_text())

    return text

def load_text(path):
    file = open(path,'r')
    text = file.read()
    file.close()
    return text

def search_text(text_list,word,n):
    result = []
    for page_number , text in enumerate(text_list):
        if(word.lower() in text.lower()):
            index = text.lower().find(word.lower())

            beginning = max(0, index - n)
            end = min(len(text), index + len(word) + n)

            clipped = text[beginning:end]

            result.append({"Page" : page_number,"Text" : clipped})

    return result


