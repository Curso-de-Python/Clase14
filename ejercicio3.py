'''
-----------------------------
 EJERCICIO N°3
 La variable __dict__
-----------------------------
'''
class ClaseEjemplo:
  varia = 1
  def __init__(self, val):
    ClaseEjemplo.varia = val

print(ClaseEjemplo.__dict__)
objetoEjemplo = ClaseEjemplo(2)

print(ClaseEjemplo.__dict__)
print(objetoEjemplo.__dict__)
