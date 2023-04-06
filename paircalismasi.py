#2. Gün Pair Çalışması

# Bir hesap makinesi kodladığımızı varsayalım, kullanıcı ilk olarak sırayla 2 adet sayı girecek ve
#  bu sayılar arasında yapmak istediği dört işlemi seçecek. Seçerken verdiği değerler
#  dört işlemden birisi değil ise kullanıcı uyarılacak ( + - * / ). 
# Girilen işleme göre bu iki sayı arasında ilgili işlem yapılarak kullanıcıya sonuç gösterilecek. 


sayi1= float(input("Birinci sayıyı giriniz: "))
sayi2=float(input("İkinci sayıyı giriniz: "))

islemSec=input("İşlem seçiniz: toplama için(+), Çıkarma için (-), Bölme için(/), Çarpma için (*) ")

if islemSec=="+":
    sonuc=sayi1+sayi2
    print("Toplamı: ",sonuc)
elif islemSec=="-":
    sonuc=sayi1-sayi2
    print("Çıkarma:", sonuc)
elif islemSec=="*":
    sonuc=sayi1*sayi2
    print("Çarpma:", sonuc)
elif islemSec=="/":
    sonuc=sayi1/sayi2
    print("Bölümü:",sonuc)
else:
    print("Dört işlemden birini seçiniz")



