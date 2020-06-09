from .PersonajePrecavido import PersonajePrecavido
from ..Mixins.Evita_problemas import Evita_problemas
class PersonajePrecavidoEvitaProblemas(Evita_problemas,PersonajePrecavido):
    def que_hago(self):
        if(self.hay_enemigo_mas_energico()):
            return self.celda
        