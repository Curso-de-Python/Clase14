'''
-----------------------------
 EJERCICIO N°1
 Variables de instancia
-----------------------------
'''
class ClaseEjemplo:
  def __init__(self, val = 1):
    self.primera = val

  def setSegunda(self, val):
    self.segunda = val

objetoEjemplo1 = ClaseEjemplo()
objetoEjemplo2 = ClaseEjemplo(2)

objetoEjemplo2.setSegunda(3)

objetoEjemplo3 = ClaseEjemplo(4)
objetoEjemplo3.tercera = 5

print(objetoEjemplo1.__dict__)
print(objetoEjemplo2.__dict__)
print(objetoEjemplo3.__dict__)

# ¿Y si vuelves las variables a variables privadas?