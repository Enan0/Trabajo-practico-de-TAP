from ..Personaje import Personaje


class PersonajeColaborador(Personaje):
    def buscar_aliados(self):
        
        cantidad_compañeros = 0
        # Guarda las celdas vecinas
        celdas_vecinas = self.celda.dame_celdas_vecinas()

    # Recorre las celdas de alrededor
        for celda in celdas_vecinas:
            personajes = celda.dame_personajes()
            # Si la lista de personajes es vacia continua con la siguiente iteracion
            if(personajes == []):
                continue

            # Recorre la lista de personajes de la celda
            for personajeI in personajes:
                
                # Si el personaje es enemigo continua con la siguiente iteracion
                if(personajeI.dame_jugador() != self.dame_jugador()):
                    continue
                

                cantidad_compañeros += 1
        if(cantidad_compañeros < 2):
            return False
        
        return True
