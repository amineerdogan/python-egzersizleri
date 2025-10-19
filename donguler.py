#for=> list

sayilar=[3,5,7,2,12,32,45]
for i in sayilar:
    print(i)
print("-")
#"sayilar" listesindeki hangi sayilar 3 ün katıdır.
for x in sayilar:
    if x%3==0:
        print(x)
# sayilar listesindeki tüm sayiların toplamı nedir
print("--")
toplam=0
for y in sayilar:
  toplam+=y
print(toplam)
  
urunler = ["iphone 13, samsung s24", "samsung s22", "iphone 15", "iphone 14"]

for urun in urunler:
    if "iphone" in urun:
        print(urun.index("iphone"))
    else:
        print("iphone bulunamadı:", urun)

print("*********")
urunler=[
    {"urunAdi":"Hp Victus","fiyat":32999},
    {"urunAdi":"Lenovo ThimkPad","fiyat":25499},
    {"urunAdi":"Apple Macbook","fiyat":26999},
    {"urunAdi":"Casper Nirvana","fiyat":20000}
]
#1-Aşağıdaki örnek cümleyi tüm ürünlere uygulayın:
#"HP Victus marka ürünün fiyatı 32999 Türk Lirası."
for urun in urunler:
    print(f"{urun['urunAdi']} marka ürünün fiyatı {urun['fiyat']} Turk Lirası")
    #2- urunlerin fiyatları toplamı:
    print("********************")
toplam=0
for x in urunler:
    toplam=toplam +x['fiyat']
print(f"tüm ürünlerin toplamı: {toplam}")

#3-25000 ile 40000 arasındaki ürünleri listeleyiniz.
for m in urunler:
    if m['fiyat']>25000 and m["fiyat"]<40000:
        print(f"urunun fiyatı koşulu sağlıyor: {m['urunAdi']}")
    else:
        print(f"urun koşulu sağlamıyor {m['urunAdi']}")
#4-Kullanıcıdan alınan anahtar kelimeye göre ürünleri listeleyiniz.



#while=>koşullu
