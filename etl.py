#modulo para guardar as funções da pipiline

import pandas as pd #importa a biblioteca pandas com o apelido pd, é uma biblioteca de manipulação de dados em python
import os
import glob

#função que ler e concatenas arquivos json
def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    """
    Função que extrai os dados de todos os arquivos json em uma pasta e os
    consolida em um único dataframe.

    Parameters
    ----------
    pasta : str
        Caminho da pasta com os arquivos json

    Returns
    -------
    pd.DataFrame
        Dataframe consolidado
    """
    arquivos = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos]
    df = pd.concat(df_list, ignore_index=True)
    return df

#função que transforma
def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Essa função calcula o total de vendas de cada produto, multiplicando a quantidade de cada produto
    pela sua venda e adiciona essa informação em uma coluna chamada "Total" no dataframe que
    é passado como parâmetro.

    Args:
        df (pd.DataFrame): Dataframe com as informações de quantidade e venda de cada produto

    Returns:
        pd.DataFrame: Dataframe com a coluna "Total" adicionada.
    """
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

#uma função para load em csv ou parquet
#parametro que vai ser ou 'csv' ou 'parquet' ou ainda uma lista com os dois
def carregar_dados(df: pd.DataFrame, format_saida: list):
    '''Função para salvar o dataframe em csv e/ou parquet'''
    for formato in format_saida:
        if formato == 'csv':
            df.to_csv('data.csv', index=False)
        elif formato == 'parquet':
            df.to_parquet('data.parquet', index=False)

def pipeline_calcula_kpi_de_vendas_consolidado(pasta: str, format_saida: list):
    """
    Função que executa a pipeline de extração, transformação e carregamento dos dados
    """
    df = extrair_dados_e_consolidar(pasta)
    df_calculado = calcular_kpi_de_total_de_vendas(df)
    carregar_dados(df_calculado, format_saida)

if __name__ == '__main__':
    pipeline_calcula_kpi_de_vendas_consolidado("data", ['csv', 'parquet'])

