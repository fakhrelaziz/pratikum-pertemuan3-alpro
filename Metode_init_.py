"""
Semua kelas memiliki metode bawaan yang disebut __init__() __init__(), yang selalu dieksekusi saat kelas diinisialisasi, digunakan untuk menetapkan nilai pada properti object saat obejct sedang dibuat
metode bisa juga dikatakan function, dinamakan metode karena function berada didalam sebuah class
"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Fakhrel", 20)

print(p1.name)
print(p1.age)

#Tanpa metode
class Person:
  pass

p1 = Person() #mengatur properti secara manual
p1.name = "Fakhrel"
p1.age = 20

#Menetapkan nilai default pada metode
class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Azir")
p2 = Person("Fakhrel", 20)

print(p1.name, p1.age)
print(p2.name, p2.age)



