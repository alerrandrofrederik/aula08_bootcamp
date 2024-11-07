from etl import pipeline_calcula_kpi_de_vendas_consolidado

pasta = 'data'
format_saida = ['csv', 'parquet']

pipeline_calcula_kpi_de_vendas_consolidado(pasta, format_saida)
