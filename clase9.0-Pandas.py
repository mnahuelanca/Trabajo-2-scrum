import pandas as pd
import numpy as np


# Datos con valores nulos
datos = {
    'NOMBRE': ['GLORIA','INDIRA','VICTOR','LUIS', np.nan],
    'EDAD': [np.nan, 34, 31, 30, 27],
    'CARRERA': ['SISTEMAS', 'COMUNICACION', 'SISTEMAS', 'MECANICA', 'MATEMATICAS']
}

# Convierto Serie en Dataframe
df = pd.DataFrame(datos)
print(df)
print('\n')

# Identificar valores faltantes
print(df.isnull().sum())
print(df.isna().sum())
print(f'\n{df.isna().sum()}')
print('\n')

# Eliminando filas con NaN
dfSinNan = df.dropna()
print(dfSinNan)
print('\n')

# Agregar fila al DataFrame. (Igual a 'LUIS')
df.loc[4] = ['LUIS', 30, 'MECANICA'] # Duplicado
print(df) # 2 luis
print('\n')

# Identificar y eliminar registros duplicados
dfSinDuplicados = df.drop_duplicates()
print(dfSinDuplicados) # 1 luis
print('\n')

# Borrar fila de una columna en particular
#dfSinDupliColumna = df.drop_duplicates(subset=['NOMBRE'])
#print(dfSinDupliColumna)
print('\n')

