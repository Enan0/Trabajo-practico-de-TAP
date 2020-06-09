# pylint: disable=maybe-no-member

class Evita_problemas(object):
    def BuscarCelda_ConMenos_ataque(self):
        # 1 Obtener las celdas vecinas
        # 2 Obtener jugadores de las celdas vecinas
        # 3 Recorrer celdas vecinas
        # 4 Sumar la cantidad de daño de la celda
        # 5 Comparar con otra celda
        celdas_vecinas = self.celda.dame_celdas_vecinas()
        tmp_potencia_de_ataque = 0

        #Recorremos las celdas vecinas
        for celda in celdas_vecinas:
            
            # Obtenemos los personajes de la 'celda'
            personajes_de_la_celda = celda.dame_personajes()
            total_potencia_de_celda = 0
            if(personajes_de_la_celda == []):
                # Si esta vacio saltamos la iteracion
                continue
            #Recorremos los personajes de la celda
            for personaje in personajes_de_la_celda:
                
                # Comprueba que no son aliados
                if(personaje.dame_jugador() == self.dame_jugador()):
                    continue

                # Suma la potencia_de_ataque
                total_potencia_de_celda += personaje.potencia_de_ataque()

            if(total_potencia_de_celda > tmp_potencia_de_ataque):
                tmp_potencia_de_ataque = total_potencia_de_celda
            sugerencia_celda = celda
        return sugerencia_celda

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
        # Guarda todas las celdas vecinas
        celdas_vecinas = self.celda.dame_celdas_vecinas()
        # Recorre las celdas
        for celda in celdas_vecinas:
            personajes_en_celda = celda.dame_personajes()
            celdas_ocupadas = []

            if(personajes_en_celda == []):
                # En caso de que una celda este vacia, automaticamente no estamos rodeados
                return False

            '''
                Recorremos la lista de personajes en celda y si hay un personaje enemigo
                agrega la celda en la lista de celdas_ocupadas
            '''
            for personaje in personajes_en_celda:
                # Si el personaje es aliado si iguiente iteracion
                if(personaje.dame_jugador() == self.dame_jugador()):
                    continue

                celdas_ocupadas.append(celda)
                break

        # Si las listas son iguales significa que las celdas vecinas estan todas ocupadas
        if(celdas_ocupadas == celdas_vecinas):
            return True
        return False
