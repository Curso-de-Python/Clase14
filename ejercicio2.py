'''
-----------------------------
 EJERCICIO N°2
 Variables de clase
-----------------------------
'''
class ClaseEjemplo:
  contador = 0
  def __init__(self, val = 1):
    self.__primera = val
    ClaseEjemplo.contador += 1

objetoEjemplo1 = ClaseEjemplo()
objetoEjemplo2 = ClaseEjemplo(2)
objetoEjemplo3 = ClaseEjemplo(4)

print(objetoEjemplo1.__dict__, objetoEjemplo1.contador)
print(objetoEjemplo2.__dict__, objetoEjemplo2.contador)
print(objetoEjemplo3.__dict__, objetoEjemplo3.contador)

# ¿Y si convertirmos "contador" en una variable privada?
