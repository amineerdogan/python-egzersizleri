kurum="BTK AKADEMİ".split()
print(type(kurum))
print(kurum)

sayilar=[1,2,3,4,5]
print(type(sayilar[0])) 

ogrenci=["amine", "erdoğan",60,75,25]
print(ogrenci[0]+" "+ogrenci[1])
ortalama=(ogrenci[2]+ogrenci[3]+ogrenci[4])/3
print(ortalama)

ogrenciler=[["amine", "Erdoğan",50,25,85],["esma","Turan",65,89,97]]
print(ogrenciler[0][1])
print(ogrenciler[1][2])

programlama_diller=["phyton","C#","Java","JavaScript"]

sonuc=programlama_diller
sonuc=type(programlama_diller)
sonuc=programlama_diller[0:2]
sonuc=programlama_diller[:2]
sonuc=programlama_diller[1:]
sonuc=programlama_diller[2:-3]

#güncelleme 
programlama_diller[-1]="React"
print(programlama_diller)

#LİSTE UYGULAMALARI
#1- "Toyota","BMV","Renault","Mercedes" elemanlarına sahip markalar isimli bir liste oluştur.
markalar=["Toyota","BMV","Renault","Mercedes"]

#2- Liste kaç elemanlıdır
sonuc=len(markalar)

#3- Lİstenin ilk ve son elemanı nedir?
markalar[0]
markalar[-1]

#4-"Renault" markasını "Togg" ile güncelleyiniz.
markalar[2]="Togg"
print(markalar) 

#5-"Togg" listenin bir elemanı mıdır?
sonuc="Togg" in markalar

#6- listenin ilk iki elemanını alınız
sonuc=markalar[0:2]

#7- listenin sonuna "Ford" ve "Citroen" markalarını ekleyin.
sonuc=markalar+["Ford","Citroen"]

#8- Listenin son elemanını silelim
del markalar[-1]
sonuc=markalar

#9-
ogrenci1=["yiğit","Bilgi",2010,[70,80,90]]
ogrenci2=["Ada","Bilgi",2012,[70,70,80]]
ogrenci3=["Çınar","Turan",2017,[60,60,90]]
ogrenciler=[ogrenci1,ogrenci2,ogrenci3]

#10-ogrencilerin yaşını hesaplayınız
yasYigit=2025-ogrenci1[2]
yasAda=2025-ogrenci2[2]
yasCinar=2025-ogrenci3[2]
print(yasYigit,yasAda,yasCinar) 

#11-Ogrencilerin not ortalamalarını hesaplayın
yigitNot=(ogrenciler[0][3][0]+ogrenciler[0][3][1]+ogrenciler[0][3][2])/3
print(yigitNot)
 

 #LİSTE METOTLARI
sayilar=[1,2,3,4,5,6,7]
isimler=["amine","esma","ayşe","yusuf","ali"]

sonuc=min(sayilar)
sonuc=min(isimler)

sayilar.append(12)
sonuc=sayilar
isimler.append("merve")
sonuc=isimler

sayilar.insert(0,100)
sayilar.insert(-1,100)
sayilar.insert(len(sayilar),100)

#silme
sayilar.pop()
sayilar.pop(0)
sayilar.pop(-2)
isimler.pop(0)
isimler.remove("esma")

#sıralama
sayilar.sort()
isimler.sort()

sayilar.reverse()
isimler.reverse()


sonuc=isimler.count("merve")

print(sonuc)

#LİSTELER İLE İLGİLİ UYGULAMA
customer=["sadikTuran","ahmetYilmaz","cinarTuran","yiğitBilgi"]
ordertotals=[12000,13000,5000,15000]

#1- sadıturan kullanıcı adıyla yapılan 5000 liralık siparişi listeye ekleyin
customer.append("SadıkTuran")
ordertotals.append(5000)
print(customer)
print(ordertotals)

#2- son eklenen siparişi siliniz
customer.pop()
ordertotals.pop()
print(customer)
print(ordertotals)

#3- Tüm müşteriler için aşağıdaki özet cümleyi yazdırınız
#'<username>' isimli müşterinin sipariş toplamı '<10000>' liradır.
print(customer[0]+" isimli müşterinin sipariş toplamı "+str(ordertotals[0])+" liradır.")
print(customer[1]+" isimli müşterinin sipariş toplamı "+str(ordertotals[1])+" liradır.")
print(customer[2]+" isimli müşterinin sipariş toplamı "+str(ordertotals[2])+" liradır.")

#4- Müşterileri alfabetik olarak sıralayın
customer.sort()
print(customer)
ordertotals.sort()
print(ordertotals)

#5-en düşük sipariş hangisidir?
min(ordertotals)
customer.append("sadikTuran")

#6-Sadık turan adlı kullanıcıcn kaç tane siparişi vardır
print(customer.count("sadikTuran"))

#7- customer listesinden ahmetYilmaz adlı kullanıcıyı siliniz
customer.remove("ahmetYilmaz")
print(customer)

#8- kullanıcıdan aldığımız kullanıcı adı ve sipariş toplamlarını listeye ekleyiniz
userName=input("kullanıcı adı: ")
toplam=input("toplam:" )
customer.append(userName)
ordertotals.append(toplam)
print(ordertotals)
print(customer)


#DİCTİONARY
ogrenciler={
    101:{"Ad":"yiğit",
         "soyad":"Bilgi",
         "dogumYili":2010,
         "notlar:":(40,80,90)},

    102:{
        "Ad":"Ada",
         "soyad":"Bilgi",
         "dogumYili":2012,
         "notlar:":(80,80,80),
    },
    103:{"Ad":"Çınar",
         "soyad":"Turan",
         "dogumYili":2017,
         "notlar:":(70,70,70),}
}

yemekTarifi= {
    "yemekAdi":"Musakka",
    "yemekTarifi":"tarifaçıklaması",
    "resim" : "1.jpg"
}
yemekTarifi.get("yemekAdi")
yemekTarifi.keys()
yemekTarifi.values()
yemekTarifi.items()
yemekTarifi.update({"yemekAdi":"Mantı"})
yemekTarifi.popitem()