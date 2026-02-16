"""
Properti adalah variabel yang dimiliki oleh suatu class. Properti menyimpan data untuk setiap objek yang dibuat dari class tersebut
"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Fakhrel", 20)

print(p1.name)#mengakses proprty objek dengan titik
p1.age = 26 # mengubah nilai property
print(p1.age)
del p1.age #menghapus property

"""
Properti yang didefinisikan di luar metode merupakan milik kelas itu sendiri (properti kelas) dan dimiliki bersama oleh semua objek, artinya semua objek memilik property sama, oleh karena itu memodifikasi properti kelas dapat memengaruhi semua objek:

"""
class Person:
  species = "Human" # Class property

"""
Properti yang didefinisikan di dalamnya __init__()merupakan milik setiap objek (properti instans).

"""
  def __init__(self, name):
    self.name = name # Instance property

#menambahkan property baru ke object yang sudah ada
p1 = Person("Fakhrel")
p1.age = 20
p1.city = "Pekanbaru"

