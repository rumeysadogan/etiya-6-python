#döngüler -start

# for i in range(len(ogrenciler)):
#     if i==3:
#         break
#     print(f"{i+1}. Öğrenci: {ogrenciler[i]}")

#pass => ilgili alanın bodysini boş bırakabilmemize olanak sağlar
# for i in range(0,10):
#     pass

#continue => iterasyondaki current değeri atla, bir sonraki değer ile devam et
# for i in ogrenciler:
#     if i=="Volkan":
#         continue
#     print(f"Öğrenci:{i}")


#while booleanDeğer 
# infinite loop-sonsuz döngü  belirli bir şartı bir 
# CTRL+C => terminali durduran manuel işlem

# i=0
# while i<10:
#     i=i+1
#     if i==3:
#         break
#     print(f"While içerisindeki i değeri: {i}") 
    
#döngüler - loops - end 

# fonksiyonlar - start

#defination

def ortalamaHesaplama():
    final = 100
    vize= 100
    ortalama = (vize *0.4)+(final*0.6)
    print(ortalama)

def ortalamaHesaplamaVeDondur(vize,final) -> float:
    return (vize *0.4)+(final*0.6)
    #expression returnden sonra yazdığımız kısma deniyor
    #geriye dönmek

#triggerlamak, çalıştırmak, execute etmek, methodu çağırmak, fonksiyonu çağırmak
ortalamaHesaplama()
benimOrtalamam2=ortalamaHesaplama() # -> None değeri
print(ortalamaHesaplamaVeDondur(100,60))
print(ortalamaHesaplamaVeDondur(70, 100))
print(benimOrtalamam2)