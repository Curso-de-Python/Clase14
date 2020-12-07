# MÉTODOS A DETALLE
# Parámetro self
class conClase:
  def metodo(self):
    print("método")

obj = conClase()
obj.metodo()

'''
# Parámetros adicionales
class conClase:
  def metodo(self, par):
    print("método:", par)

obj = conClase()
obj.metodo(1)
obj.metodo(2)
obj.metodo(3)

#-------------------------
# EL CONSTRUCTOR __init__
class conClase:
  def __init__(self, valor):
    self.var = valor

obj1 = conClase("objeto")

print(obj1.var)
'''
