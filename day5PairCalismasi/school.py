
from student import Student
from teacher import Teacher

studentList=[]
teacherList=[]
def studentAdd(studentName,studentNumber,studentAge):
    ogrenci=Student(studentName,studentNumber,studentAge)
    studentList.append(ogrenci)
def teacherAdd(teacherName,teacherTelNumber,teacherAge):
    ogretmen=Teacher(teacherName,teacherTelNumber,teacherAge)
    teacherList.append(ogretmen)

studentAdd("Süeda", 321, 26)
studentAdd("Ayşe", 246, 25)
studentAdd("Gökçem", 853, 24)
studentAdd("Rümeysa", 796, 20)

teacherAdd("Halit Enes Kalaycı", 5559996633, 25)
teacherAdd("Engin Demiroğ", 5551112233, 30)

print("Öğrenciler : ")
for ogrenci in studentList:
    ogrenci.studentShow()
print(" ")
print("Öğretmenler : ")
for ogretmen in teacherList:
    ogretmen.teacherShow()