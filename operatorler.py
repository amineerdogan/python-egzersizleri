#a,b,c=4,8,(12,2)
#toplam=a+b+(c[0]+c[1])
#x=int(input("lütfen bir sayı giriniz:"))
#y=int(input("lütfen bir sayı giriniz:"))

#arpim=x*y
#fark = carpim - toplam

#print("Çarpım:", carpim)
#print("Toplam:", toplam)
#print("Fark:", fark)


#girilen iki sayıdan hangisi büyüktür
#sayi1=input("birinci sayi:")
#sayi2=input("ikinci sayi:")
#onuc=(sayi1>sayi2)
#print(f"{sayi1}{sayi2} den buyuk {sonuc}")

#1- Yaşı 18'den büyük ya da veli izni varsa bir işte çalışabilir durumunu kontrol ediniz.
#veliİzni=True
#yas=17
#sonuc=(veliİzni or yas>=18)

#2- Ders Notu 50-100 arasındaysa geçti değilse kaldı bilgisini yazınız.
#dersNotu=50
#sonuc=(dersNotu>=50 and dersNotu<=100)

#3-Not Ortalaması en az 70 puan ve zayıfı yoksa teşekkür belgesi alabilme durumunu kontrol ediniz
#notOrtalaması=75
#zayifSayisi=0
#sonuc=(ortalama>=70) and(zayifSayisi==0)
#print(sonuc)

# KOSULLU DURUMLAR
# 1. aracın yakıt tipine göre (benzin, dizel, lpg) belirtilen bir mesafede ne kadar yakıt harcanacağını hesapla

yakit = input("Lütfen yakıt tipini giriniz (benzin/dizel/lpg): ")
mesafe = float(input("Lütfen gidilen mesafeyi yazınız: "))

if yakit == "benzin":
    yakit_masrafi = mesafe * 39.35
elif yakit == "dizel":
    yakit_masrafi = mesafe * 41.71
else:
    yakit_masrafi = mesafe * 20.28

print("Toplam yakıt masrafı:", yakit_masrafi, "TL")
