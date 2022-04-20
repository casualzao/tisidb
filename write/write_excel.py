import os
import easyocr
import tesserocr
from PIL import Image
import pytesseract
from tesserocr import PyTessBaseAPI
from PIL import Image

import openpyxl

from openpyxl import Workbook

cru_path = "/Users/p.c.m.d/develop/project-python/tisidb/data/"
x_trip = {'ACC': 'B', 'BLCA': 'C', 'BRCA': 'D', 'CESC': 'E', 'CHOL': 'F', 'COAD': 'G', 'ESCA': 'H', 'GBM': 'I',
          'HNSC': 'J',
          'KICH': 'K', 'KIRC': 'L', 'KIRP': 'M', 'LGG': 'N', 'LIHC': 'O',
          'LUAD': 'P', 'LUSC': 'Q', 'MESO': 'R', 'OV': 'S', 'PAAD': 'T', 'PCPG': 'U', 'PRAD': 'V', 'READ': 'W',
          'SARC': 'X',
          'SKCM': 'Y', 'STAD': 'Z', 'TGCT': 'AA', 'THCA': 'AB', 'UCEC': 'AC',
          'UCS': 'AD',
          'UVM': 'AE'}

y_trip = {'BTNL2': '2', 'C10orf54': '3', 'CD27': '4', 'CD276': '5', 'CD28': '6', 'CD40': '7', 'CD40LG': '8',
          'CD48': '9',
          'CD70': '10', 'CD80': '11', 'CD86': '12', 'CXCL12': '13', 'CXCR4': '14', 'ENTPD1': '15', 'HHLA2': '16',
          'ICOS': '17',
          'ICOSLG': '18', 'IL2RA': '19', 'IL6': '20', 'IL6R': '21', 'KLRC1': '22', 'KLRK1': '23', 'LTA': '24',
          'MICB': '25', 'NT5E': '26', 'PVR': '27','RAET1E': '28','TMEM173': '29',
          'TMIGD2': '30',
          'TNFRSF13B': '31',
          'TNFRSF13C': '32',
          'TNFRSF14': '33',
          'TNFRSF17': '34',
          'TNFRSF18': '35',
          'TNFRSF25': '36',
          'TNFRSF4': '37',
          'TNFRSF8': '38',
          'TNFRSF9': '39',
          'TNFSF13': '40',
          'TNFSF13B': '41',
          'TNFSF14': '42',
          'TNFSF15': '43',
          'TNFSF18': '44',
          'TNFSF4': '45',
          'TNFSF9': '46',
          'ULBP1': '47'}

reader = easyocr.Reader(['en'], gpu=True)




def read():
    db = open("/Users/p.c.m.d/develop/project-python/tisidb/write/tisdb.txt")
    line = db.readline()
    book = openpyxl.load_workbook("/Users/p.c.m.d/develop/project-python/tisidb/write/tisdb3.xlsx")
    r_sheet = book['r']
    p_sheet = book['p']

    while line:
        if line.__contains__('parse') or line.__contains__("None"):
            err = line.strip().lstrip().split(" ")
            # if line.__contains__("parse"):
            #     ocr(err[2])
            line = db.readline()
            continue
        try:
            data = line.strip().replace(",", "").split(" ")
            x = data[0]
            y = data[1]
            clo = x_trip.get(x)
            row = y_trip.get(y)
            rho = data[4]
            p = data[7]
            r_sheet[clo + row] = rho
            p_sheet[clo + row] = p
        except BaseException:
            print(x + "+" + y + ".jpg")

        line = db.readline()

    book.save("/Users/p.c.m.d/develop/project-python/tisidb/write/tisdb3.xlsx")


def new_ocr(img_url):
    image = Image.open(cru_path + img_url)
    code = pytesseract.image_to_string(image, lang='eng')
    text = str(code).split("Test")
    if len(text) == 2:
        print(text[1].replace("\n", '').replace("\f", "").replace(":", "").replace(",", ""))
    print("parse error", img_url)


def te_ocr(img_url):
    image = Image.open(cru_path + img_url)
    print(tesserocr.image_to_text(image))  # print ocr text from image


def ocr(img_url):
    test = reader.readtext(cru_path + img_url, detail=0)
    text = str(test).split("Test")
    if len(text) == 2:
        name = img_url.split('.')[0].split("+")
        print(name[0], name[1], test[len(test) - 1])
    else:
        print("parse error", img_url)


if __name__ == '__main__':
    read()
