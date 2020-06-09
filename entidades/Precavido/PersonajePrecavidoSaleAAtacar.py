from .PersonajePrecavido import PersonajePrecavido
from ..Mixins.Sale_a_atacar import Sale_a_atacar

class PersonajePrecavidoSaleAAtacar(Sale_a_atacar,PersonajePrecavido):
    def que_hago(self):
        if(self.hay_enemigo_mas_energico() == True):
            return self.BuscarCelda_ConMenos_ataque()
        return self.celda
