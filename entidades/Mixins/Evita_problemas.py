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

    def buscar_celda_sinEnemigos(self):
        """
            Busca una celda vecina sin enemigos
        """
        #Guarda las celdas vecinas
        celdas_vecinas = self.celda.dame_celdas_vecinas()
        celda_sugerida = None

        for celda in celdas_vecinas:

            personajes = celda.dame_personajes()

            if(personajes == []):
                #Si en esta celda no hay personajes automaticamente guarda la celda actual
                celda_sugerida = celda

            #Recorre los personajes de la celda
            for personajeI in personajes:

                #Si el personaje es enemigo rompe el ciclo y busca en otra celda
                if(personajeI.dame_jugador() != self.dame_jugador()):
                    break

            celda_sugerida = celda
        return celda_sugerida

    def estamos_rodeados(self):
        """
            Comprueba si en las celdas vecinas hay enemigos
        """
        # Obtiene las cedlas vecinas
        celdas_vecinas = self.celda.dame_celdas_vecinas()

        lista_celdas_con_enemigos = []

        # Recorremos las celdas vecina
        for celda in celdas_vecinas:

            # Guarda los personajes
            personajes = celda.dame_personajes()

            # Si no hay personajes en la lista devuelve false
            # Ya que lo que estamos comprobando es si estamos o no rodeados
            if(personajes == []):
                return False

            #Recorre los personajes de la celda
            for personaje in personajes:

                #Si el personaje es de un equipo diferente
                # Guarda la celda actual en la lista de celdas con enemigos
                if(personaje.dame_jugador() != self.dame_jugador()):
                    lista_celdas_con_enemigos.append(celda)
                continue

        # Si la lista de celdas con enemigos adentro 
        # Es diferente a celdas vecinas devuelve False
        if(lista_celdas_con_enemigos != celdas_vecinas):
            return False

        return True
