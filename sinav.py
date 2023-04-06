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

