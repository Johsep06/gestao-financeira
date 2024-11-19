import json

def salvar_em_json(lista_dicionarios, caminho_arquivo):
    """
    Salva uma lista de dicionários em um arquivo JSON.

    :param lista_dicionarios: List[dict] - Lista de dicionários a ser salva.
    :param caminho_arquivo: str - Caminho do arquivo JSON onde os dados serão salvos.
    """
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(lista_dicionarios, arquivo, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")


def ler_de_json(caminho_arquivo):
    """
    Lê uma lista de dicionários de um arquivo JSON.

    :param caminho_arquivo: str - Caminho do arquivo JSON a ser lido.
    :return: List[dict] - Lista de dicionários carregada do arquivo.
    """
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        return dados
    
    except FileNotFoundError:
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump([], arquivo, ensure_ascii=False, indent=4)
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        return dados
    
    except Exception as e:
        return []
