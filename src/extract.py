import requests


class extract:

    def __init__(self):
        pass

    def extract_data(self, country: str) -> list[dict]:
        """
        Método responsável por extrair os dados da API e transformar em uma lista com dicionários.
        
        Args:
            country: str - Nome do país que será pesquisado na API.

        """

        url = f"http://universities.hipolabs.com/search?country={country}"

        response = requests.get(url)
        response.raise_for_status()  
        universities = response.json()

        return universities