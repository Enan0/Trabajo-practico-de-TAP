"""EDITS"""
from entorno.Tableros_especiales.TableroCuadrado import TableroCuadrado
"""EDITS"""
# TESTS PARA TABLERO CUADRADO Y CELDA

tablero0 = TableroCuadrado(0)
tablero1 = TableroCuadrado(1)
tablero2 = TableroCuadrado(2)
tablero4 = TableroCuadrado(4)

celda0 = tablero4.dame_celdas()[0]
celda1 = tablero4.dame_celdas()[1]
celda2 = tablero4.dame_celdas()[2]

# Verificando creacion de tableros cuadrados
assert len(tablero0.dame_celdas()) == 0
assert len(tablero1.dame_celdas()) == 1
assert len(tablero2.dame_celdas()) == 4
assert len(tablero4.dame_celdas()) == 16

# Chequeando celdas creadas
assert celda0.dame_coordenadas() == {'x':0, 'y':0}
assert celda1.dame_coordenadas() == {'x':0, 'y':1}
assert celda2.dame_coordenadas() == {'x':0, 'y':2}

# Chequeando celdas vecinas
assert tablero4.son_vecinas(celda0,celda1)
assert celda1 in celda0.dame_celdas_vecinas()
assert celda0 in celda1.dame_celdas_vecinas()
assert tablero4.son_vecinas(celda1,celda2)
assert celda2 in celda1.dame_celdas_vecinas()
assert celda1 in celda2.dame_celdas_vecinas()
assert not tablero4.son_vecinas(celda0,celda2)
assert not celda2 in celda0.dame_celdas_vecinas()
assert not celda0 in celda2.dame_celdas_vecinas()

# Agregando personajes
assert len(celda0.dame_personajes()) == 0
celda0.agregar_personaje("un personaje de mentirita")
assert len(celda0.dame_personajes()) == 1
celda0.agregar_personaje("otro personaje de mentirita")
assert len(celda0.dame_personajes()) == 2
