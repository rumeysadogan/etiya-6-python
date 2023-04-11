print("Merhaba Dünya")
print("Hoş geldiniz")
# yorum satırı 

# değişkenler start

text="Merhaba"

print(text)
print(text)
text="Selam"
print(text)
print(text)

studentCount = 45 
print(studentCount + 5)

averagePoint=25.5 # double, float, ondalıklı sayılar
print(averagePoint + 5)

isVerified= True # bool, boolean
print(isVerified)

print(type(text))
print(type(studentCount))
print(type(averagePoint))
print(type(isVerified))
#değişkenler end

#operatörler start

number =10 
#matematiksel operatörler - mantıksal operatörler
print(10 + 10 )
print(number + number)
print(number -5 )
print(number /2) #tam bölünse dahi float türünde geri dönüş yapar
print(number*5)

# mod operatörü  => sol tarafındaki değerin sağ tarafındaki değere bölümünden kalan sonuç
print(number % 3)

print(number + ((10-number)*(5/10)))

#mantıksal operatörler - karşılaştırma operatörleri 
print(number==10) #true
print(10 != 10) #false
print(number>10)    #false
print(number>=10) #true

#operatörler end
print("***************************** 06NISAN2023 ********************************")

#diziler - listeler - start
sayilar=[100,200,300,400,500, "Merhaba", 15.5, True]
print(sayilar[0])
print(sayilar[5])

# 

print(sayilar)
sayilar.append(600) #append fonksiyonu liste sonnuna eleman ekler
print(sayilar)
sayilar.pop()   #pop fonksiyonu liste sonundaki default son elemanı siler
print(sayilar)
sayilar.remove("Merhaba") # pop'un aksine indexe göre değil değere göre siler
print(sayilar)
sayilaraEkleme=[700,800,900]
sayilar.extend(sayilaraEkleme) #append'in aksine tek bir değer değil listedeki tüm elemanları listeye ekler
print(sayilar)
#diziler - listeler - end


#string interpolation -start 
hello="Merhaba"
userName="Rümeysa"
totalText=hello+ " " + userName
print(totalText)

totalText=" {message} Sevgili {name}".format(message=hello, name=userName)
print(totalText)

#f-string
totalText= f"Hoşgeldiniz {userName}"
print(totalText)
#string interpolation - end 

# karar yapıları - start
ortalamaNot= input("Lütfen ortalamanızı giriniz: ")

#numerik => int, double
#type conversion -start
ortalamaNotAsInteger = int(ortalamaNot)
#type conversion -end

#if else blokları
# 4 satır => 1tab/indent

#indent
if ortalamaNotAsInteger >50:
    print("Bravo")
   # if ortalamaNotAsInteger >80:
    #    print("Geçtiniz")
elif ortalamaNotAsInteger >60:
    print("Ortalama")
elif ortalamaNotAsInteger > 50:
    print("Normal")
else:
    print("Maalesef")
    print("Kaldınız")

studentCount = 44
if studentCount >20:
    print("Öğrenciler ders için hazır")

print("If bloğundan bağımsız kısım")

print("****************** ÖDEV *******************")
vize = float(input("Vize notunuzu giriniz: "))
final= float(input("Final notunuzu giriniz: "))
ortalama= float((vize*0.4)+(final*0.6))
if final < 40:
    print("Kullanıcı Kaldı")
elif ortalama < 50:
    print("Kullanıcı Kaldı")
elif vize == (final * 2):
    print("Kullanıcı Kaldı")
else:
    print("Kullanıcı geçti")

# eğer final 40'dan küçükse kullanıcı kaldı
# eğer ortalama 50'den küçükse kullanıcı kaldı
# eğer vize finalin 2 katı ise kullanıcı kaldı
# bunun dışındaki tüm durumlarda kullanıcı geçti yazdırmak istiyoruz

#daha kısa yolu böyle yapabilirsin
if final < 40 or ortalama <50 or vize ==final*2:
    print("Kaldı")
else:
    print("Geçti")
# karar yapıları - end

#07.04.2023 sabah workshop u *******************************************************************

# Ödev kontrol yapılıyoooorrr -start Workshop3 ister 1
biggestValue=0 
for i in range(10):
    sayi=int(input(f"{i+1}. sayıyı giriniz: "))
    if sayi>biggestValue:
        biggestValue=sayi
print(f"Girdiğiniz sayılar arasından en büyük olanı: {biggestValue}")

# Workshop3 ister 2
sayilar=[]
for i in range(10):
    sayilar.append(int(input(f"{i+1}. sayıyı giriniz: ")))
# print(min(sayilar))
# print(max(sayilar))
# sayilar.sort() #küçükten büyüğe sıralar
sayilar.sort(reverse=True) #büyükten küçüğe sıralar
enBuyukN=int(input("Sayılar arasından kaçıncı elemanı istiyorsun? "))
print(sayilar[enBuyukN - 1])

#3. ister => 2. isterdeki alt limit kullanıcı belirlemelidir
forRangeMin =int(input("Döngünün alt limitini belirleyiniz: "))
forRangeMax =int(input("Döngünün üst limitini belirleyiniz: "))
for i in range(forRangeMin, forRangeMax+1):
    if i % 2==0:
        print(i)
## end

