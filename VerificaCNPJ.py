import pandas as pd
import requests
from pprint import pprint
from brutils import is_valid_cnpj, remove_symbols_cnpj


class VerificadorDeCnpj:
    def __init__(self, dataset):
        self.dataset = dataset
        self.brasil_api = 'https://brasilapi.com.br/api/cnpj/v1/'

    def consulta_brasil_api(self, cnpj):
        dicionario_cnpj = requests.get(url=f"{self.brasil_api}/{cnpj}").json()
        return dicionario_cnpj

    def valida_cnpj(self, cnpj):
        for self.cnpj in self.dataset:
            if not is_valid_cnpj(cnpj):
                print(f'{cnpj} é um CNPJ inválido! Verifique o CNPJ e tente novamente.')
                return False
            else:
                return True

    def sanitiza_cnpj(self, cnpj):
        for self.cnpj in self.dataset:
            cnpj = remove_symbols_cnpj(cnpj)
            return cnpj


if __name__ == '__main__':
    VerificadorDeCnpj = VerificadorDeCnpj(dataset=['27.865.757/0001-02'])
    cnpj = VerificadorDeCnpj.sanitiza_cnpj(cnpj='27.865.757/0001-02')
    if VerificadorDeCnpj.valida_cnpj(cnpj):
        pprint(VerificadorDeCnpj.consulta_brasil_api(cnpj))
