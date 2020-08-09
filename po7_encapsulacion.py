class CasillaDeVotacion:
    
    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = 'Estuve aqui'

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if region in self._pais:
            print('Estuve aqui 2')
            self._region = region
        else:
            print('Estuve aqui 3')
            raise ValueError(f'La region {region} no esta en la lista')


casilla = CasillaDeVotacion(123,['Mexico','Morelos'])
print(casilla.region)
casilla.region = 'Mexico'
print(casilla.region)
casilla.region = 'Peru'


