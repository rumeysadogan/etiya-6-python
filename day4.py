# Aşağıdaki programı geliştiriniz: 
# Kullanıcıyı sürekli konsolda tutarak istediği kadar işlem yapmasını sağlayacak bir hesap makinesi
# programlayacağız. Hesaplama işlemlerinin her biri ayrı fonksiyon olmalıdır.
# Kullanıcı klavyeden ilk olarak istediği işlemi ( + - / * % ) girmelidir. 
# Dört işleme ek mod hesaplama da dahil. Daha sonra gireceği iki sayının kullanıcının 
# istediği işleme yönlendirilmesini eğer kullanıcıdan alınan değer yukarıdaki beş sembolden biri değilse
# programın hata vermesini sağlayalım. Kullanıcı işlem seçmek yerine “q” harfi girişi yaparsa programı 
#  sonlandıralım aksi takdirde program her hesaplama sonrası tekrar işlem yapabilir olmalıdır.

def Toplama():
    sayi1 = int(input("1. Sayı: "))
    sayi2 = int(input("2. Sayı: "))
    print("sonuc=",sayi1,"+",sayi2,"=", sayi1+sayi2 )
 
# Çıkarma Fonksiyonu
def Cikarma():
    sayi1 = int(input("1. Sayı: "))
    sayi2 = int(input("2. Sayı: "))
    print("sonuc=",sayi1,"-",sayi2,"=", sayi1-sayi2)
 
# Çarpma Fonksiiyonu
def Carpma():
    sayi1 = int(input("1. Sayı: "))
    sayi2 = int(input("2. Sayı: "))
    print("sonuc=",sayi1,"*",sayi2,"=", sayi1*sayi2)
 
# Bölme Fonksiyonu
def Bolme():
    sayi1 = int(input("1. Sayı: "))
    sayi2 = int(input("2. Sayı: "))
    print("sonuc=",sayi1,"/",sayi2,"=", sayi1/sayi2)

# Mod Fonksiyonu
def Mod():
    sayi1 = int(input("1. Sayı: "))
    sayi2 = int(input("2. Sayı: "))
    print("sonuc=",sayi1,"%",sayi2,"=", sayi1%sayi2)
 
print("Yapılacak İşlemi Seçin.")

# Kullanıcıdan Seçim İsteme
islem = 0

while islem==0:
    secim = input("Seçiminiz (+ - * % / ):")

    if secim == "q":
        print("Programdan çıkılıyor...")
        islem=1

    elif secim == '+':
        Toplama()
    
    elif secim == '-':
        Cikarma()
    
    elif secim == '*':
        Carpma()
    
    elif secim == '/':
        Bolme()

    elif secim == '%':
        Mod()

    else:
        print("Hatalı giriş yaptınız")