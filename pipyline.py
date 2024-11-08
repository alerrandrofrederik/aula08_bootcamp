from etl import pipeline_calcula_kpi_de_vendas_consolidado

pasta = 'data'
formato_de_saida = ['csv', 'parquet']

pipeline_calcula_kpi_de_vendas_consolidado(pasta, formato_de_saida)
