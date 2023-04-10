

                                     # 4. PAIR ÇALIŞMASI 

# fibonacci

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


# mükemmel sayi

sayiGir=int(input("Bir Sayı Giriniz: "))
toplam=0
for i in range(1,sayiGir):
    if sayiGir%i==0:
        toplam+=i

if toplam==sayiGir:
    print("Mükemmel Sayı! ")
else:
    print("Mükemmel Sayı Değildir! ")
