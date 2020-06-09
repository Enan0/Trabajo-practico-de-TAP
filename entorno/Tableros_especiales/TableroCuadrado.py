"""Edits"""
from ..Tablero import Tablero
from ..Celda import Celda
"""Edits"""

class TableroCuadrado(Tablero):
  
  def __init__(self,dimension): # considerando la dimension indicada, genero
                                # todas las celdas e identifico sus vecinas
    self.celdas = []

    for coordx in range(dimension): 
      for coordy in range(dimension):

        nueva_cel = Celda({'x':coordx,'y':coordy}) # nueva celda

        for celda in self.celdas:

          if self.son_vecinas(nueva_cel,celda): # si son vecinas las agrego mutuamente como tal
            celda.agregar_vecina(nueva_cel) 
            nueva_cel.agregar_vecina(celda)

        self.celdas.append(nueva_cel) # agrego nueva celda al tablero

  def dame_celdas(self):
    return self.celdas

  def son_vecinas(self,celda1,celda2): # dadas dos celdas del tablero, veo si son vecinas
                                      # precondicion: las dos celdas deben pertenecer al tablero
    coord1 = celda1.dame_coordenadas()
    coord2 = celda2.dame_coordenadas()

    vecinas_horizontal = (coord1['x'] == coord2['x']) and (abs(coord1['y'] - coord2['y']) == 1)
    vecinas_vertical = (coord1['y'] == coord2['y']) and (abs(coord1['x'] - coord2['x']) == 1)

    return (vecinas_horizontal or vecinas_vertical)

