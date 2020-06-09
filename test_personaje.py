"""EDITS"""
from entidades.Personaje import Personaje
from entorno.Tableros_especiales.TableroCuadrado import TableroCuadrado


tablero0 = TableroCuadrado(0)
tablero1 = TableroCuadrado(1)
tablero2 = TableroCuadrado(2)
tablero4 = TableroCuadrado(4)

celda0 = tablero4.dame_celdas()[0]
celda1 = tablero4.dame_celdas()[1]
celda2 = tablero4.dame_celdas()[2]
"""EDITS"""


# TESTS PARA PERSONAJE
celda1.vaciar_personajes()
celda2.vaciar_personajes()
personaje0 = Personaje("Alan Turing", celda1)
personaje1 = Personaje("Ada Lovelace", celda1)
personaje2 = Personaje("Ada Lovelace", celda2)

# Personajes en celdas
assert len(celda1.dame_personajes()) == 2
assert len(celda2.dame_personajes()) == 1
assert personaje0 in celda1.dame_personajes()
assert personaje1 in celda1.dame_personajes()
assert personaje2 in celda2.dame_personajes()

# Personajes instanciados
assert personaje0.dame_jugador() == "Alan Turing"
assert personaje0.dame_celda() is celda1
assert personaje0.dame_energia() == 100
assert personaje0.dame_escudo() == 100
assert personaje0.dame_experiencia() == 0

#Potencias
assert personaje0.potencia_de_ataque() == 33.333333333333336
assert personaje0.potencia_de_defensa() == 110