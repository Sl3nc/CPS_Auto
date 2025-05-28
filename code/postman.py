from requests import get, exceptions
from json import loads

class Correios:
    """
    Consulta informações de endereço a partir do CEP usando a API ViaCEP.
    """
    URL = 'https://viacep.com.br/ws/{0}/json/'

    def __init__(self) -> None:
        pass

    def pesquisar_cep(self, endereco):
        """
        Realiza consulta do CEP e retorna dados do endereço.
        """
        try:
            url = get(self.URL.format(endereco)).content
            dic = loads(url)
            return [dic["logradouro"], dic["bairro"], dic["localidade"], dic["estado"]]
        except exceptions.ConnectionError:
            raise Exception('Falha de conexão aos sistemas dos Correios, verifique sua rede e tente novamente')
        except:
            raise Exception('Verifique se o cep foi digitado corretamente e tente novamente') 
