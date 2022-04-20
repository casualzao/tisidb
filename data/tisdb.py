import requests
from bs4 import BeautifulSoup
import xlrd
import xlwt
import os
from PIL import Image
import pytesseract

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}

x = ['ACC', 'BLCA', 'BRCA', 'CESC', 'CHOL', 'COAD', 'ESCA', 'GBM', 'HNSC', 'KICH', 'KIRC', 'KIRP', 'LGG', 'LIHC',
     'LUAD', 'LUSC', 'MESO', 'OV', 'PAAD', 'PCPG', 'PRAD', 'READ', 'SARC', 'SKCM', 'STAD', 'TGCT', 'THCA', 'UCEC',
     'UCS', 'UVM']
y = ['BTNL2', 'C10orf54', 'CD27', 'CD276', 'CD28', 'CD40', 'CD40LG', 'CD48', 'CD70', 'CD80', 'CD86', 'CXCL12', 'CXCR4',
     'ENTPD1', 'HHLA2', 'ICOS', 'ICOSLG', 'IL2RA', 'IL6', 'IL6R', 'KLRC1', 'KLRK1', 'LTA', 'MICB', 'NT5E', 'PVR',
     'RAET1E', 'TMEM173', 'TMIGD2', 'TNFRSF13B', 'TNFRSF13C', 'TNFRSF14', 'TNFRSF17', 'TNFRSF18', 'TNFRSF25', 'TNFRSF4',
     'TNFRSF8', 'TNFRSF9', 'TNFSF13', 'TNFSF13B', 'TNFSF14', 'TNFSF15', 'TNFSF18', 'TNFSF4', 'TNFSF9', 'ULBP1']

x1 = ['ACC', 'BLCA']
y2 = ['BTNL2', 'C10orf54']

pic_url = "	http://cis.hku.hk/TISIDB/"
cru_path = os.getcwd() + "/"


def download(x_item, y_item):
    base_url = "http://cis.hku.hk/TISIDB/immunomodulator_scatter.php?gene=CSMD2&group=Immunostimulator&type=exp" \
               "&cancer=" + x_item + "&target=" + y_item + "&submit=Plot"
    response = requests.get(base_url)
    if response.status_code == 200:
        return response.text
    return None


def paser(html, x_i, y_i):
    soup = BeautifulSoup(html, "html.parser")
    for img in soup.select('img'):
        img_path = img.get('src')
        re = requests.get(pic_url + img_path)
        img_name = x_i + "+" + y_i + ".jpg"
        with open(img_name, 'wb') as file:
            file.write(re.content)
        return img_name


# def ocr(img_url):
#     test = reader.readtext(cru_path + img_url, detail=0)
#     rp = test[len(test) - 1].split(',')
#     return rp

def new_ocr(img_url):
    image = Image.open(img_url)
    code = pytesseract.image_to_string(image)
    text = str(code).split("Test")
    if len(text) == 2:
        return text[1].replace("\n", '').replace("\f", "").replace(":", "")
    print("parse error", img_url)




def write_excel(workbook, x_i, x, y_i, y, rp):
    r = rp[0].split('=')[1]
    p = rp[1].split('=')[1]
    rho_sheet = workbook.get_sheet('rho')
    rho_sheet.write(x + 1, y, x_i)
    rho_sheet.write(x, y + 1, y_i)
    rho_sheet.write(x + 1, 0, r)
    p_sheet = workbook.get_sheet('p')
    p_sheet.write(x + 1, y, x_i)
    p_sheet.write(x, y + 1, y_i)
    p_sheet.write(x_i, y_i, p)


def write_txt(x_i, y_i, rp):
    print(x_i, y_i, rp)
    # if None is not rp:
    #     rp_z = str(rp).split(",")
    #     r_n = rp_z[0].split('=')[1]
    #     p_n = rp_z[1].split('=')[1]
        # with open("r.txt", "w") as r:
        #     st = x_i + y_i + r_n
        #     r.write(st)
        # with open("p.txt", "r") as p:
        #     st = x_i + y_i + p_n
        #     p.write(st)


def init():
    workbook = xlwt.Workbook(encoding='ascli')
    workbook.add_sheet('rho')
    workbook.add_sheet('p')
    return workbook


def dispatcher():
    # workbook = init()
    for i_n, x_i in enumerate(x):
        for y_n, y_i in enumerate(y):
            html = download(x_i, y_i)
            img_name = paser(html, x_i, y_i)
            if None is img_name:
                continue
            rp = new_ocr(img_name)
            # write_excel(workbook, x_i, i_n, y_i, y_n, rp)
            # print(x_i, y_i, [rp])
            write_txt(x_i, y_i, rp)
    # workbook.save("tisidb.xls")


if __name__ == '__main__':
    dispatcher()
