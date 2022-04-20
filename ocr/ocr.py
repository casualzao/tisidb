
import tesserocr
from tesserocr import PyTessBaseAPI
cru_path = "/Users/p.c.m.d/develop/project-python/tisidb/data/"
images = ['BLCA+CD276.jpg','BLCA+CD48.jpg','BLCA+CD80.jpg','BLCA+CD86.jpg','BLCA+IL6R.jpg','BLCA+KLRC1.jpg','BLCA+RAET1E.jpg','BLCA+TNFRSF14.jpg','BLCA+TNFRSF8.jpg','BLCA+TNFSF15.jpg','BLCA+TNFSF4.jpg','BRCA+C10orf54.jpg','BRCA+CD28.jpg','BRCA+CD86.jpg','BRCA+CXCL12.jpg','BRCA+KLRC1.jpg','BRCA+PVR.jpg','BRCA+TNFRSF14.jpg','BRCA+TNFRSF4.jpg','BRCA+TNFSF13B.jpg','BRCA+TNFSF9.jpg','BRCA+ULBP1.jpg','CESC+CD27.jpg','CESC+CD28.jpg','CESC+CD40.jpg','CESC+CD48.jpg','CESC+ENTPD1.jpg','CESC+ICOSLG.jpg','CESC+PVR.jpg','CESC+TNFRSF13B.jpg','CESC+ULBP1.jpg','COAD+CD28.jpg','COAD+CD48.jpg','COAD+IL6R.jpg','COAD+KLRC1.jpg','COAD+KLRK1.jpg','COAD+TNFRSF13B.jpg','COAD+TNFRSF8.jpg','COAD+TNFSF13B.jpg','COAD+TNFSF9.jpg','ESCA+CD70.jpg','ESCA+LTA.jpg','ESCA+TNFRSF4.jpg','GBM+CD276.jpg','GBM+CXCR4.jpg','GBM+IL6R.jpg','HNSC+CD276.jpg','HNSC+CD40.jpg','HNSC+CD40LG.jpg','HNSC+IL6R.jpg','HNSC+MICB.jpg','HNSC+TNFRSF13B.jpg','HNSC+TNFRSF13C.jpg','HNSC+TNFRSF25.jpg','HNSC+TNFRSF9.jpg','KIRC+PVR.jpg','KIRC+TNFRSF18.jpg','KIRC+TNFSF14.jpg','KIRC+TNFSF15.jpg','KIRP+CD48.jpg','KIRP+IL2RA.jpg','KIRP+MICB.jpg','KIRP+TNFSF13B.jpg','LGG+C10orf54.jpg','LGG+CD276.jpg','LGG+TNFRSF14.jpg','LIHC+CD28.jpg','LIHC+CD80.jpg','LIHC+TNFSF13.jpg','LUAD+CD276.jpg','LUAD+CD70.jpg','LUAD+CD80.jpg','LUAD+ENTPD1.jpg','LUAD+ICOS.jpg','LUAD+IL2RA.jpg','LUAD+IL6R.jpg','LUAD+TNFRSF14.jpg','LUAD+TNFRSF25.jpg','LUAD+TNFSF4.jpg','LUSC+CD28.jpg','LUSC+CD40LG.jpg','LUSC+CD80.jpg','LUSC+CXCR4.jpg','LUSC+ICOSLG.jpg','LUSC+TNFRSF8.jpg','LUSC+TNFSF13.jpg','LUSC+TNFSF14.jpg','OV+CD80.jpg','PCPG+TNFSF9.jpg','PRAD+CD27.jpg','PRAD+CD48.jpg','PRAD+CXCR4.jpg','PRAD+ICOSLG.jpg','PRAD+IL6.jpg','PRAD+IL6R.jpg','SARC+CD27.jpg','SARC+CD28.jpg','SARC+IL6R.jpg','SARC+TMEM173.jpg','SKCM+C10orf54.jpg','SKCM+CD48.jpg','SKCM+CXCR4.jpg','SKCM+KLRK1.jpg','SKCM+PVR.jpg','SKCM+TMIGD2.jpg','STAD+CD40LG.jpg','STAD+KLRC1.jpg','STAD+TNFRSF9.jpg','STAD+TNFSF13B.jpg','STAD+TNFSF15.jpg','TGCT+TNFSF13.jpg','THCA+C10orf54.jpg','THCA+CD70.jpg','THCA+ICOS.jpg','THCA+LTA.jpg','THCA+TNFRSF9.jpg','THCA+TNFSF13B.jpg','UCEC+ENTPD1.jpg','UCEC+LTA.jpg','UCEC+TNFRSF14.jpg','UCEC+TNFRSF18.jpg','UCEC+TNFRSF25.jpg','UCEC+TNFRSF4.jpg','UCEC+TNFSF14.jpg']

with PyTessBaseAPI() as api:
    for img in images:
        api.SetImageFile(cru_path+img)
        print(api.GetUTF8Text())
        print(api.AllWordConfidences())

if __name__ == '__main__':
    PyTessBaseAPI()