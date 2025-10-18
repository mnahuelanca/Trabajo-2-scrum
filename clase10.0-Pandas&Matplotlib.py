# Seleccion de datos

# Seleccion con CORCHETES y NOMBRES DE COLUMNAS
import pandas as pd

# DF ventas

datos = {
    "PRODUCTOS": ['LAPTOP','TECLADO','MOUSE','MONITOR','LAPTOP'],
    "CANTIDAD": [2,5,10,3,1],
    "PRECIO_UNITARIO": [1200,50,25,300,1200]
}

df = pd.DataFrame(datos)
print(df)
print('\n')

# Seleccionar multiples columnas
df_filtrado = df[['PRODUCTOS','PRECIO_UNITARIO']]
print(df_filtrado)
print('\n')

# Seleccion de filas basada en condicion
# Operadores -> Logicas (AND, OR, NOT), -> Relacionales (< > >= ...)
df_filtrado_dos = df[df['PRECIO_UNITARIO'] > 100]
print(df_filtrado_dos)
print('\n')

# Filtro con multiples condiciones
df_filtrado_tres = df[(df['PRODUCTOS'] == 'LAPTOP') & (df['CANTIDAD'] > 1)]
print(df_filtrado_tres)
print('\n')

# Creacion y agregacion de columnas
# Creo nueva columna
df['TOTAL_VENTAS'] = df['CANTIDAD'] * df['PRECIO_UNITARIO']
print(df)
print('\n')

# Agregacion con GROUPBY
# Metodo .reset_index(), convierte el resultado del groupby en un "Dataframe"
df_agrupado = df.groupby('PRODUCTOS')['TOTAL_VENTAS'].sum().reset_index()
print(df_agrupado)
print('\n')

unidades_vendidas = df.groupby('PRODUCTOS')['CANTIDAD'].sum().reset_index()
print(unidades_vendidas)
# hacer lo mismo con el titanic


