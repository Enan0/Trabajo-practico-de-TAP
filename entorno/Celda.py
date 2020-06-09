class Celda(object):

  def __init__(self,coordenadas):
    self.coordenadas = coordenadas
    self.celdas_vecinas = []
    self.personajes = []

  def dame_coordenadas(self):
    return self.coordenadas

  def dame_celdas_vecinas(self):
    return self.celdas_vecinas

  def dame_personajes(self):
    return self.personajes

  def agregar_vecina(self,una_celda):
    self.celdas_vecinas.append(una_celda)

  def agregar_personaje(self,un_personaje):
    self.personajes.append(un_personaje)

  # SOLO PARA LOS TESTS, DESESTIMAR PARA EL FUNCIONAMIENTO NORMAL
  def vaciar_personajes(self): 
    self.personajes = []