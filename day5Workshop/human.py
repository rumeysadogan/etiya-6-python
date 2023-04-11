#class
#modules 
#paket yönetimi
#self (istediğini yazabilirsin. Fakat bir parametre girilmek zorunda) => diğer programlardaki (this) devamı aşağıda
#ilgili fonk. tanımlandığı nesnenin kendisini ifade ediyor. ilk parametresi self parametresiyle rezerve ediliyor.

class Human:
    #built-in  #constructor  #initialize
    def __init__(self,name):
        self.name=name
        print("Bir  human instance'i üretildi")
    def __str__(self):      # -> str ilgili fonk geriye ne dönmesini istiyorsak
        return f"STR Fonksiyonundan dönen değer: {self.name}" 
        #pass
    def talk(self,sentence):
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking..")
