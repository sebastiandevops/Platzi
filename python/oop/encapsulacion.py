#!/usr/bin/env python3

class CasillaDeVotacion:
    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(f"la region {region} no es valida en\
                    {self._pais}")


if __name__ == "__main__":
    casilla = CasillaDeVotacion(123, ['Mexico', 'Morelos'])
    casilla._region = 'Mexico'
    print(casilla.region)
    casilla.region = 'Ciudad de Mexico'
    print(casilla.region)
