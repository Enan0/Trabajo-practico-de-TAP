from ..Personaje import Personaje


class PersonajePrecavido(Personaje):
    # CAMBIAR EL NOMBRE DE ESTE METODO EN UN FUTURO, ES MUY MALO xd
    def hay_enemigo_mas_energico(self):
        """
                Busca enemigos en las celdas vecinas donde los enemigos tengan mas energia que nosotros
                si hay un enemigo mas energico devuelve True
        """
        # Guarda las celdas vecinas
        celdas_vecinas = self.celda.dame_celdas_vecinas()
        for celda in celdas_vecinas:

            #Siempre que busque en un bucle "existe_amenaza" es true
            existe_amenaza = True
            cantidad_total_energia = 0
            personajes = celda.dame_personajes()

            # Verifica que la lista tenga indices
            if(personajes == []):
                continue

            for personajeI in personajes:
                #Si el personaje no es enemigo sigue con el bucle
                if(personajeI.dame_jugador() == self.dame_jugador()):
                    continue

                # Si alguno de los personajes de la celda tiene mas o igual energia
                # directamente rompe el bucle y busca en la siguiente celda,la celda se vuelve una amenaza
                if(self.dame_energia() <= personajeI.dame_energia()):
                    break
                
                cantidad_total_energia += personajeI.dame_energia()

                #Si la cantidad total de energia de la celda es mayor rompe el bucle y busca en la siguiente celda
                if(cantidad_total_energia >= self.dame_energia()):
                    break
            existe_amenaza = False #Si consigue terminar el ciclo de personajes existe_amenaza es False

        return existe_amenaza