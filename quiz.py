import re

kata = ('@asd11_')
cocok = re.findall(r'@+[a-zA-Z]+[0-9]+\_$', kata)
if cocok :
    print("pass")
else:
    print("failed")


##soal = """We are hiring Test/QA Engineers with 1-3 years of experience in Manual Testing(Web, Mobile & API). If anyone((Especially who lost the job due to COVID) looking for a change, please share me the resume at mailmesiva25@gmail.com
##Company:Open Financial Technologies
##Location: Bangalore
##Note: Fintech Experience would be a higher priority"""
##
##carikata = re.findall(r'[\w\.]+@+[\w\.]+', soal)
##print(carikata)

##
##class SimpulPohonBiner(object):
##    def __init__(self,data):
##        self.data = data
##        self.kanan = None
##        self.kiri = None
##A = SimpulPohonBiner('Ambarawa')
##B = SimpulPohonBiner('Bantul')
##C = SimpulPohonBiner('Cimahi')
##D = SimpulPohonBiner('Denpasar')
##E = SimpulPohonBiner('Enrekang')
##F = SimpulPohonBiner('Flores')
##G = SimpulPohonBiner('Garut')
##H = SimpulPohonBiner('Halmahera Timur')
##I = SimpulPohonBiner('Indramayu')
##J = SimpulPohonBiner('Jakarta')
##
##A.kiri = B ; A.kanan = C
##B.kiri = D ; B.kanan = E
##C.kanan = F
##E.kiri = G
##G.kanan = H
##H.kiri = I
##
##def tampilLuarKanan(pohon):
##    if pohon.kanan is not None:
##        tampilLuarKanan(pohon.kanan)
##    print(pohon.data)
##def tampilLuarKiri(pohon):
##    if pohon.kiri is not None:
##        tampilLuarKiri(pohon.kiri)
##    print(pohon.data)
##
##tampilLuarKana(A)
##tampilLuarKiri(A)




    
