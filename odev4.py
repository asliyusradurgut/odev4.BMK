#1- kendisine gönderilen kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.
def yazma():
    for i in range(5):
        print("aslı")
yazma()
#2- dikdörtegen alan ve çevresini hesaplayan fonksiyonu yazınız.
kenar1= 10
kenar2= 20
def cevre():
    return (10+20)*2
sonuc1= cevre()
print(sonuc1)
 
def alan():
    return 10*20
sonuc2= alan()
print(sonuc2)

#3-yazı tura uygulamasını fonksiyon kullanarak yapınız.(random modülü)
import random

def yazi_tura():
    sonuc = random.choice(['Yazı', 'Tura'])
    return sonuc
print(yazi_tura()) 

#4- kendisine gönderilen 2 sayı arasındal-ki tüm asal sayıları bulan fonksiyonu yazınız
sayi1=10
sayi2=25
def aradaki_asal_sayilar(sayi1, sayi2):
    def asal_kontrol(sayi):
        if sayi < 2:  
            return False
        for i in range(2, int(sayi ** 0.5) + 1):  
            if sayi % i == 0:
                return False
        return True
    baslangic = min(sayi1, sayi2) + 1
    bitis = max(sayi1, sayi2)
    return [sayi for sayi in range(baslangic, bitis) if asal_kontrol(sayi)]
print(aradaki_asal_sayilar(sayi1,sayi2))
#5- kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde dödüren fonksiyonu yazınız.
sayi=30
def tamBolen(sayi):
    return [i for i in range(1, sayi + 1) if sayi % i == 0]
print(tamBolen(sayi))




