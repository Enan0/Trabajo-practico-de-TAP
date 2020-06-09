class Personaje(object):
    energia = 100
    escudo = 100
    experiencia = 0

    def __init__(self,jugador,celda_donde_estoy):
        self.jugador = jugador
        self.celda = celda_donde_estoy
        self.celda.agregar_personaje(self)

    def dame_escudo(self):
        return self.escudo

    def dame_energia(self):
        return self.energia
    
    def dame_experiencia(self):
        return self.experiencia
    
    def dame_jugador(self):
        return self.jugador

    def dame_celda(self):
        return self.celda
    
    def potencia_de_ataque(self):
        
        ultima_potencia_de_ataque = (self.energia / 3) + (self.experiencia / 5)
        return ultima_potencia_de_ataque
    
    def potencia_de_defensa(self):
        
        ultima_potencia_de_defensa = self.escudo + (self.energia / 10) + (self.experiencia / 3)
        return ultima_potencia_de_defensa
