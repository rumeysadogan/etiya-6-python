# kullanıcıdan vize ve final notları alacak.
# vize %40  final %60 etkili olacak
# vize ve final notları 50.5 gibi ondalıklı sayılar olabilir
# uygulama ortalamayı hesaplayacak ve ortalamaya göre
# 0-49 FF
# 50-59 DD
# 60-69 CC
# 70-79 BB
# 80-100 AA
# not ortalamasını ve not harfini kullanıcıya gösterecek programı kodlayınız. 

vize = float(input("Vize notunuzu giriniz: "))
final = float(input("Final notunuzu giriniz: "))
ortalama = (vize * 0.4) + (final * 0.6) 

if ortalama < 50:
    print("Ortalamanız : " , ortalama,"Harf Notu : FF" )

if (ortalama > 49) and (ortalama < 60):
    print("Ortalamanız : " , ortalama,"Harf Notu : DD" )

if (ortalama > 59) and (ortalama < 70):
    print("Ortalamanız : " , ortalama,"Harf Notu : CC" )

if (ortalama > 69) and (ortalama < 80):
    print("Ortalamanız : " , ortalama,"Harf Notu : BB" )

if (ortalama > 79) and (ortalama <= 100):
    print("Ortalamanız : " , ortalama,"Harf Notu : AA" )