from human import Human
# instance => örnek. Nesnelere ulaşabilmek için bir instance oluşturmamız gerekiyor

human1=Human("Rümeysa")
human1.talk("Merhaba")
human1.walk()
print(human1)

human2=Human("Başak")
human2.talk("Selam")
human2.walk()
print(human2)

Human("Melike").talk("Merhaba")