#class , nesne , obje , sınıf 
class Human:
    #property, attribute => özellik, nitelik
    #initialize
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("yapıcı blok çalıştı")
    #davranışlar
    def talk(self, message):
        print(f"{self.name}: {message}")
    def walk(self):
        print(f"{self.name} is walking..")

#instance üretmek - örnek üretmek 
human1 = Human("Rümeysa",28)    #contructor => yapıcı blok
human1.talk("Merhaba")
human1.walk()