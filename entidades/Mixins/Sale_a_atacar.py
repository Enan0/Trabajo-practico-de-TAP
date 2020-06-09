# pylint: disable=maybe-no-member
class Sale_a_atacar(object):
    def BuscarCelda_ConMenos_defensa(self):
        """
            Guarda la defensa de nuestra celda 
            y la compara con la defensa total de las celdas vecinas
        """
        nuestra_celda = self.celda.dame_personajes()
        nuestro_valor_de_defensa = self.potencia_de_defensa()
        celda_sugerida = None
        # Recorre los personajes de nuestra celda y suma nuesta potencia de defensa
        for personajeI in nuestra_celda:
            if(personajeI.dame_jugador() != personajeI.dame_jugador()):
                # Si es enemigo recorre el siguiente personaje
                continue
            nuestro_valor_de_defensa += personajeI.potencia_de_defensa()
            
        # Guarda las celdas vecinas
        celdas_vecinas = self.celda.dame_celdas_vecinas()

        # Recorremos las celdas vecina
        for celda in celdas_vecinas:
            
            personajes = celda.dame_personajes()
            cantidad_total_de_defensa = 0

            if(personajes == []):
                # Si la celda esta vacia de personajes, recorre la siguiente celda
                continue

            for personajeI in personajes:

                if(personajeI.dame_jugador() == self.dame_jugador()):
                    # Si son aliados, recorre el siguiente personajeI
                    continue

                if(personajeI.potencia_de_defensa() >= nuestro_valor_de_defensa):
                    # Si el personajeI.potencia_de_defensa() es mayor a nuestro defensa rompe el bucle
                    # Y busca en la siguiente celda
                    break

                # 1 El personaje tiene menos defensa que nuesta cantidad de defensa
                # 2 Es enemigo
                cantidad_total_de_defensa += personajeI.potencia_de_defensa()

                if(cantidad_total_de_defensa > nuestro_valor_de_defensa):
                    # Si nuestra defensa es menor romple el bucle y busca otra celda
                    break

            celda_sugerida = celda
        return celda_sugerida
