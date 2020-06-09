from .PersonajeColaborador import PersonajeColaborador
from ..Mixins.Sale_a_atacar import Sale_a_atacar


class PersonajeColaboradorSaleAAtacar(Sale_a_atacar, PersonajeColaborador):
    def que_hago(self):
        if(self.buscar_aliados() == False):
            return self.BuscarCelda_ConMenos_defensa()
        return self.celda
