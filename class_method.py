"""
Metode adalah fungsi yang dimiliki oleh suatu class. Metode mendefinisikan perilaku objek yang dibuat dari kelas tersebut
"""

class Person:
     def __init__(self, name): #ini adalah _init_ method
          self.name = name

     def greet(self):
          print("Hello, my name is " + self.name)
    
     def multiply(self, a, b): #metode dengan parameter
          return a * b
     
     def get_info(self): #mengakses dan bisa memodifikasi obejct property
          return f"{self.name} is {self.age} years old"
     
     def __str__(self): #metode ini untuk mengatur hasil atau mengembalikan nilai apa yang diinginkan ketika object di print
          return f"{self.name} ({self.age})"

p1 = Person("Emil")
p1.greet()
del Person.greet #menghapus metode