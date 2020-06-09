"""EDITS"""
from entorno.Tableros_especiales.TableroCuadrado import TableroCuadrado

from entidades.Pancho.PersonajePancho import PersonajePancho
from entidades.Colaborador.PersonajeColaboradorSaleAAtacar import PersonajeColaboradorSaleAAtacar
from entidades.Colaborador.PersonajeColaboradorEvitaProblemas import PersonajeColaboradorEvitaProblemas
from entidades.Precavido.PersonajePrecavidoSaleAAtacar import PersonajePrecavidoSaleAAtacar
from entidades.Precavido.PersonajePrecavidoEvitaProblemas import PersonajePrecavidoEvitaProblemas
"""EDITS"""

# TESTS PARA CRITERIOS Y SUGERENCIAS

# Tablero de 4x4
tablero = TableroCuadrado(4)
celda00 = tablero.dame_celdas()[0]
celda01 = tablero.dame_celdas()[1]
celda10 = tablero.dame_celdas()[4]
celda20 = tablero.dame_celdas()[8]
celda30 = tablero.dame_celdas()[12]
celda31 = tablero.dame_celdas()[13]
celda32 = tablero.dame_celdas()[14]
celda33 = tablero.dame_celdas()[15]

# Dos jugadores, haskell y klara
haskell = "Haskell Curry"
klara = "Klara Von Neumann"

# Personajes con criterios
pers_pancho_1 = PersonajePancho(haskell, celda00)
pers_pancho_2 = PersonajePancho(haskell, celda01)
pers_pancho_3 = PersonajePancho(haskell, celda10)
pers_pancho_4 = PersonajePancho(haskell, celda32)
pers_precavido_evitar_problemas = PersonajePrecavidoEvitaProblemas(haskell, celda01)
pers_colaborador_evitar_problemas = PersonajeColaboradorEvitaProblemas(klara, celda30)
pers_precavido_sale_a_atacar = PersonajePrecavidoSaleAAtacar(klara, celda32)
pers_colaborador_sale_a_atacar = PersonajeColaboradorSaleAAtacar(klara, celda33)

# Sugerencias:

# Los panchos siempre sugieren la celda donde estan
assert pers_pancho_1.que_hago() is celda00
assert pers_pancho_2.que_hago() is celda01
assert pers_pancho_3.que_hago() is celda10
assert pers_pancho_4.que_hago() is celda32

# Estos precavidos sugieren la celda donde estan porque en ninguna 
# celda vecina hay un enemigo con mas energia que ellos
assert pers_precavido_evitar_problemas.que_hago() is celda01
assert pers_precavido_sale_a_atacar.que_hago() is celda32

# Este colaborador elige moverse porque no hay al menos 2 celdas vecinas con al menos un companiero.
# Como sale a atacar, sugiere la celda donde la defensa enemiga sea menor.
assert pers_colaborador_sale_a_atacar.que_hago() is celda32

# Este colaborador elige moverse porque no hay al menos 2 celdas vecinas con al menos un companiero.
# Como evita problemas, sugiere una celda donde no hay enemigos.
assert (pers_colaborador_evitar_problemas.que_hago() is celda20) or (pers_colaborador_evitar_problemas.que_hago() is celda31)

# Pongo un pancho de haskell en una celda vecina del colaborador que evita problemas de klara.
# Ese colaborador que evita problemas ahora sugiere la unica celda vecina sin enemigos.
pers_pancho_5 = PersonajePancho(haskell, celda20)
assert pers_colaborador_evitar_problemas.que_hago() is celda31

# Pongo otro pancho de haskell en la otra celda vecina del colaborador que evita problemas de klara.
# Ahora queda rodeado y sugiere la celda con menor potencia de ataque enemigo.
pers_pancho_6 = PersonajePancho(haskell, celda31)
# (Por este caso especial, accedemos directo a los atributos del personaje. No hagan esto en sus casas)
pers_pancho_6.energia = 1000    
pers_pancho_6.experiencia = 100 

assert pers_colaborador_evitar_problemas.que_hago() is celda20

for celda in tablero.dame_celdas():
  celda.vaciar_personajes()