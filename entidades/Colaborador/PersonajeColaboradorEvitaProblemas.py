from .PersonajeColaborador import PersonajeColaborador
from ..Mixins.Evita_problemas import Evita_problemas
class PersonajeColaboradorEvitaProblemas(Evita_problemas,PersonajeColaborador):
    def que_hago(self):
        if(self.buscar_aliados()):
            return self.celda()
            
        if(self.estamos_rodeados()):
            return self.BuscarCelda_ConMenos_ataque()
        
        return self.buscar_celdan_sinEnemigos()
