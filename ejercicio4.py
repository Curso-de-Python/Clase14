'''
-----------------------------
 EJERCICIO N°4
 Comprobando la existencia de un atributo
-----------------------------
'''
class ClaseEjemplo:
  def __init__(self, val):
    if val % 2 != 0:
      self.a = 1
    else:
      self.b = 1

objetoEjemplo = ClaseEjemplo(1)

print(objetoEjemplo.a)
print(objetoEjemplo.b)

# SOLUCIÓN 1
#try:
#  print(objetoEjemplo.b)
#except AttributeError:
#  pass

# SOLUCIÓN 2
#if hasattr(objetoEjemplo, 'b'):
#  print(objetoEjemplo.b)

'''
-----------------------------
 ¿Puedes predecir el resultado?
-----------------------------

class ClaseEjemplo:
  a = 1
  def __init__(self):
    self.b = 2

objetoEjemplo = ClaseEjemplo()

print(hasattr(objetoEjemplo, 'b'))
print(hasattr(objetoEjemplo, 'a'))
print(hasattr(ClaseEjemplo, 'b'))
print(hasattr(ClaseEjemplo, 'a'))
'''