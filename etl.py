#modulo para guardar as funções da pipiline

import pandas as pd
import os
import glob

#função que ler e concatenas arquivos json
pasta = 'data'
arquivos = glob.glob(os.path.join(pasta, '*.json'))
df_list = [pd.read_json(arquivo) for arquivo in arquivos]
df = pd.concat(df_list, ignore_index=True)
print(df)

