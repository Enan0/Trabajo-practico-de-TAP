# pylint: disable=maybe-no-member

class Evita_problemas(object):
    def BuscarCelda_ConMenos_ataque(self):
        # 1 Obtener las celdas vecinas
        # 2 Obtener jugadores de las celdas vecinas
        # 3 Recorrer celdas vecinas
        # 4 Sumar la cantidad de daño de la celda
        # 5 Comparar con otra celda
        celdas_vecinas = self.celda.dame_celdas_vecinas()
        for celda in celdas_vecinas:
            tmp = 100
            potencia_total = 0
            personajes = celda.dame_personajes()

            if(personajes == []):
                continue

            for personaje in personajes:

                if(personaje.dame_jugador() == self.dame_jugador()):
                    continue

                potencia_total += personaje.potencia_de_ataque()

                if(potencia_total <= tmp):
                    tmp = potencia_total
                    celda_sugerida = celda
                    del potencia_total

        return celda_sugerida

    def buscar_celdan_sinEnemigos(self):

        celdas_vecinas = self.celda.dame_celdas_vecinas()
        celda_sugerida = None
        for celda in celdas_vecinas:
            personajes = celda.dame_personajes()
            if(personajes == []):
                celda_sugerida = celda
            for personajeI in personajes:
                if(personajeI.dame_jugador() != self.dame_jugador()):
                    break
            celda_sugerida = celda
        return celda_sugerida

    def estamos_rodeados(self):
        celdas_vecinas = self.celda.dame_celdas_vecinas()
        lista_celdas_con_enemigos = []
        for celda in celdas_vecinas:

            personajes = celda.dame_personajes()

            if(personajes == []):
                return False

            for personaje in personajes:

                if(personaje.dame_jugador() != self.dame_jugador()):
                    lista_celdas_con_enemigos.append(celda)

                continue
        # Si la lista de celdas con enemigos sea diferente a celdas vecinas devuelve False
        if(lista_celdas_con_enemigos != celdas_vecinas):
            return False

        return True
