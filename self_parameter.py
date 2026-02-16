"""
Parameter ini self adalah referensi ke instance kelas saat ini, digunakan untuk mengakses properti dan metode yang dimiliki oleh kelas tersebut.
tidak harus bernama self, asalkan didefinisikan di parameter pertama, tetap disarankan pakai nama self
"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, nama aku " + self.name) #metod untuk mendapatkan nilai dan mencetak

p1 = Person("Fakhrel", 20)
p1.greet()

