#text="Btk Akademi Phyton Dersleri"
#sonuc=text.title()
#sonuc=text.upper()
#sonuc="abc".isupper()
#sonuc=text.split()
# print(sonuc)
# print(sonuc[0])

kursAdi="Btk Akademi Phyton ile Programllama Dersleri"
webSite="https://www.btkakademi.gov.tr/"

#1-BTK Akademi karakter dizisinin baş ve sondaki boşluk karakterini siliniz.
sonuc=" BTK Akademi ".strip()

# 2- kursAdi değişkenindeki tüm karakterleri küçük harfe çeviriniz.
sonuc=kursAdi.lower()

#3- website değişkeninde kaç tane '.' karakteri vardır.
sonuc=webSite.count('.')

# 4- webSite değişkeni 'http' ile mi başlıyor.
sonuc=webSite.startswith('https')

# 5- webSite değişkeni 'tr' ile mi bitiyor.
sonuc=webSite.endswith(tr)

# 6- kursAdi içerisindeki tüm karakterler harflerden mi oluşur.
sonuc=kursAdi.isalpha()

# 7- kursAdi değişkenindeki tüm boşluklar "-" ile değğiştirin
sonuc=kursAdi.replace(' ','-')

# 8-KursAdi değişkenindeli phyton kelimesini reactJs ile değiştirin
sonuc=kursAdi.replace('Phyton','reactJs')

# 9- webSitesi www değişkeni içeriyor mu
sonuc=webSite.find('www')

# 10- kursAdi değişkenini listeye çevir
sonuc=kursAdi.split()
print(sonuc)