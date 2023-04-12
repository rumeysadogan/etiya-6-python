# Bir okul kayıt sistemi kodlayalım;

# Öğrenci ve Öğretmen classlarını farklı dosyalarda oluşturalım. +
#  Bu classlar içerisinde en az 2 property 2 method barındırmalıdır. +
# Daha sonra bir dosyada öğrenci ve öğretmen classlarını import ederek +
#  bir listede kayıtlı öğrenci/öğretmen bilgilerini ayrı ayrı tutalım. +
#  Listeye ekleme yapan, listedeki tüm elemanları ekrana yazan fonksiyonları geliştirelim
#  ve konsolda test edelim.

# Classlarımız içerisinde self keywordü kullanalım.
# Class içi fonksiyonlarda içerideki propertylerden yararlanalım.


class Student:
    def __init__(self,studentName,studentNumber,studentAge):
        self.studentName=studentName
        self.studentNumber=studentNumber
        self.studentAge=studentAge
    
    def studentShow(self):
         print(f" - {self.studentName} adlı {self.studentNumber} numaralı {self.studentAge} yaşa sahip öğrenci listeye eklendi")


