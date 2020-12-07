'''
-----------------------------
 EJERCICIO N°5
 Usos del parámetro self
-----------------------------
'''
# Para acceder a propiedades del objeto y variables de clase
class conClase:
  varia = 2
  def metodo(self):
    print(self.varia, self.var)

obj = conClase()
obj.var = 3
obj.metodo()

# Para invocar otros métodos dentro de la clase
class conClase():
  def otro(self):
    print("otro")

  def metodo(self):
    print("método")
    self.otro()

obj = conClase()
obj.metodo()