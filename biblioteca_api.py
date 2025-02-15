import requests

class APIAula3Client:
    """
    Biblioteca para encapsular os endpoints definidos no openapi.json da 'API da Aula 3'.
    
    Exemplo de uso:
    ---------------
    from api_aula3_client import APIAula3Client
    
    # Crie o cliente informando a URL base da API e um api_token válido:
    client = APIAula3Client(base_url="http://seu-servidor.com", api_token=1234)
    
    # Para gerar uma história sobre um tema específico:
    resposta_historia = client.gerar_historia(tema="Um dia de chuva")
    print(resposta_historia)
    
    # Para testar o endpoint /operacoes/teste:
    resposta_teste = client.teste()
    print(resposta_teste)
    
    # Para somar dois números (v1 - parâmetros na URL):
    resposta_soma = client.soma_v1(numero1=10, numero2=5)
    print(resposta_soma)
    """

    def __init__(self, base_url: str, api_token: int):
        """
        Inicializa o cliente da API.

        :param base_url: URL base onde a API está rodando.
                        Exemplo: "http://localhost:8000" ou "https://api.minhaapp.com"
        :param api_token: Token de acesso exigido pela API (inteiro).
        """
        self.base_url = base_url.rstrip("/")  # Remove barra final se existir
        self.api_token = api_token

    def gerar_historia(self, tema: str) -> dict:
        """
        POST /llm/gerar_historia
        Gera uma história sobre o tema informado.
        
        :param tema: Título ou assunto para gerar a história (string).
        :return: Resposta JSON da API (normalmente um dicionário).
        """
        url = f"{self.base_url}/llm/gerar_historia"
        params = {
            "tema": tema,
            "api_token": self.api_token
        }
        resp = requests.post(url, params=params)
        resp.raise_for_status()
        return resp.json()['historia']

    def teste(self) -> dict:
        """
        GET /operacoes/teste
        Retorna mensagem de teste, confirmando se a API está funcionando.
        
        :return: Resposta JSON da API (normalmente um dicionário com mensagem).
        """
        url = f"{self.base_url}/operacoes/teste"
        params = {
            "api_token": self.api_token
        }
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        return resp.json()['mensagem']

    def soma_v1(self, numero1: int, numero2: int) -> dict:
        """
        POST /operacoes/soma/{numero1}/{numero2}
        Recebe dois números (via URL) e retorna a soma.
        
        :param numero1: Primeiro número (int).
        :param numero2: Segundo número (int).
        :return: Resposta JSON da API (normalmente um dicionário com o resultado).
        """
        url = f"{self.base_url}/operacoes/soma/{numero1}/{numero2}"
        params = {
            "api_token": self.api_token
        }
        resp = requests.post(url, params=params)
        resp.raise_for_status()
        return resp.json()['resultado']

    def soma_v2(self, numero1: int, numero2: int) -> dict:
        """
        POST /operacoes/soma/v2
        Recebe dois números (via query parameters) e retorna a soma.
        
        :param numero1: Primeiro número (int).
        :param numero2: Segundo número (int).
        :return: Resposta JSON contendo a estrutura de 'Resultado' (normalmente algo como {"resultado": <soma>}).
        """
        url = f"{self.base_url}/operacoes/soma/v2"
        params = {
            "numero1": numero1,
            "numero2": numero2,
            "api_token": self.api_token
        }
        resp = requests.post(url, params=params)
        resp.raise_for_status()
        return resp.json()

    def soma_v3(self, numero1: int, numero2: int) -> dict:
        """
        POST /operacoes/soma/v3
        Recebe dois números no corpo da requisição (JSON) e retorna a soma.
        
        :param numero1: Primeiro número (int).
        :param numero2: Segundo número (int).
        :return: Resposta JSON contendo a estrutura de 'Resultado'.
        """
        url = f"{self.base_url}/operacoes/soma/v3"
        params = {
            "api_token": self.api_token
        }
        json_body = {
            "numero1": numero1,
            "numero2": numero2
        }
        resp = requests.post(url, params=params, json=json_body)
        resp.raise_for_status()
        return resp.json()['resultado']

    def divisao(self, numero1: int, numero2: int) -> dict:
        """
        POST /operacoes/divisao/{numero1}/{numero2}
        Recebe dois números (via URL) e retorna a divisão (numero1 / numero2).
        
        :param numero1: Primeiro número (int).
        :param numero2: Segundo número (int).
        :return: Resposta JSON contendo o resultado.
        """
        url = f"{self.base_url}/operacoes/divisao/{numero1}/{numero2}"
        params = {
            "api_token": self.api_token
        }
        resp = requests.post(url, params=params)
        resp.raise_for_status()
        return resp.json()

    def operacao(self, numero1: int, numero2: int, tipo: str) -> dict:
        """
        POST /operacoes/operacao
        Recebe dois números e o tipo de operação, retornando o resultado.
        
        :param numero1: Primeiro número (int).
        :param numero2: Segundo número (int).
        :param tipo: Tipo de operação (pode ser "soma", "subtracao", "multiplicacao" ou "divisao").
        :return: Resposta JSON contendo o resultado.
        """
        url = f"{self.base_url}/operacoes/operacao"
        params = {
            "tipo": tipo,        # soma / subtracao / multiplicacao / divisao
            "api_token": self.api_token
        }
        json_body = {
            "numero1": numero1,
            "numero2": numero2
        }
        resp = requests.post(url, params=params, json=json_body)
        resp.raise_for_status()
        return resp.json()
