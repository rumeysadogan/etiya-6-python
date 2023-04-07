#döngüler -start

for i in range(len(ogrenciler)):
    if i==3:
        break
    print(f"{i+1}. Öğrenci: {ogrenciler[i]}")

#pass => ilgili alanın bodysini boş bırakabilmemize olanak sağlar
for i in range(0,10):
    pass

#continue => iterasyondaki current değeri atla, bir sonraki değer ile devam et
for i in ogrenciler:
    if i=="Volkan":
        continue
    print(f"Öğrenci:{i}")


#while booleanDeğer 
# infinite loop-sonsuz döngü  belirli bir şartı bir 
# CTRL+C => terminali durduran manuel işlem

i=0
while i<10:
    i=i+1
    if i==3:
        break
    print(f"While içerisindeki i değeri: {i}") 
    
#döngüler - loops - end 
