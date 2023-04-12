#classes.py içindeki Human'ı kullan
#import classes => tüm classes modülünü import eder
from classes import Human # => classes modülünden Human'ı import
import random #pythondaki hazır modüller
#alias =>takma ad
#from classes import Human as Insan
#import classes as classlarım
human1=Human("Rümeysa",28)
human1.talk("Selam")
print(random.random())