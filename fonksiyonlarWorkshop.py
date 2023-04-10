# Workshop - 10.04.2023
# Aşağıdaki python kursumuzun "Fonksiyonları Anlayalım" kısmını izleyip uygulayınız.
# Sonrasında tek bir dosya oluşturarak şu ana kadar yaptığınız çalışmalarınızdaki işlevleri
# (3.gündeki fibonacci vb..) fonksiyonlar haline getirerek kodlayınız.


                                            #fibonacci
def fibonacciFonksiyonu():
    fibonacciList=[]
    sayiBir=1
    sayiIki=0
    toplam=0 
    for i in range(20):
        toplam=sayiBir+sayiIki
        sayiBir=sayiIki
        sayiIki=toplam
        fibonacciList.append(toplam)
    print(fibonacciList)
fibonacciFonksiyonu()
fibonacciFonksiyonu()
                                           # mükemmel sayı
def mükemmelSayiFonksiyonu():
    sayiGir=int(input("Bir Sayı Giriniz: "))
    toplam=0
    for i in range(1,sayiGir):
        if sayiGir%i==0:
            toplam+=i
    if toplam==sayiGir:
        print("Mükemmel sayı! ")
    else:
        print("Mükemmel sayı değildir")
mükemmelSayiFonksiyonu()
mükemmelSayiFonksiyonu()
mükemmelSayiFonksiyonu()
                                #Kullanıcıdan Girilen 10 adet sayı Max? Min?
def enBuyukSayiFonksiyonu():
    sayilar=[]
    for i in range(3):
        i=int(input("Bir Sayı Giriniz: "))
        sayilar.append(i)
    print(sayilar)
    enBuyukDegisken=max(sayilar)
    print("En büyük sayı ", enBuyukDegisken)
enBuyukSayiFonksiyonu()
enBuyukSayiFonksiyonu()
                                                 # Çift Sayılar
def ciftSayiFonksiyonu():
    ustLimit=int(input("Üst Limit Sayıyı Belirle: "))
    for ciftsayi in range(0, ustLimit, 2):
        print(ciftsayi)

    altLimit=int(input("Alt Limiti Belirleyiniz: "))

    for ciftsayi in range(altLimit, ustLimit):
        if ciftsayi%2==0:
            print("Belirlediğiniz Çift Sayılar:  ", ciftsayi)
ciftSayiFonksiyonu()