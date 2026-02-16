"""
Class itu seperti blueprint untuk membuat objek bisa juga dikatakan seperti template dalam membuat suatu objet

"""
#Membuat Class
class MyClass:
     a = 7 # a ini adalah properti atau atribut

#Membuat Object
p1 = MyClass()
print(p1.a)
#Hapus object
del p1
#dapat membuat beberapa object
p2 = MyClass()
p3 = MyClass()

#pernyataan pass
"""
class tidak boleh kososng artinya class harus memiliki propert, jika tidak ingin mendefinisikan maka gunakan pass 
"""
class Person:
  pass

