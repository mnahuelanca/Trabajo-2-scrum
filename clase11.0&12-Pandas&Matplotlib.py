# Clase 11 y 12

#Matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# Configurar visualizacion de dataframe completo (columnas, filas y datos)
pd.set_option('display.max_column', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)

# Usando Try Except
try:
    df = pd.read_csv('train.csv')
    print('Dataset cargado exitosamente')
    #print(df.head())
    
except FileNotFoundError:
    'Archivo no encontrado'
print('\n')

# Verificamos valores nulos
#print(df.isnull().sum())
print("Registro nulos de Edad")
print(df['Age'].isnull().sum())
print('\n')

# Eliminar valores nulos
df_sin_edad_nulos = df.dropna(subset='Age')
print("Registro nulos de Edad, actualizado")
print(df_sin_edad_nulos['Age'].isnull().sum())
print('\n')

# Histograma (edad)
# 1. Creamos espacio/lienzo para el grafico
#                   Col,Fil
plt.figure(figsize=(10,6))
plt.hist(df_sin_edad_nulos['Age'], bins=20, color='gray', edgecolor='black')

# Titulos de ejes
plt.title('Distribucion de las edad de los pasajeros del Titanic')
plt.xlabel('Edades')
plt.ylabel('Cantidad')


# Mostrar grafico
#plt.show()

# Grafico de barras (sobrevivientes por clases)
# Agrupamos los datos por sobrevivientes por clase
sob_por_clase = df.groupby('Pclass')['Survived'].sum()
print(sob_por_clase)

# Convierto serie anterior a un Dataframe
df_sob_por_clase = sob_por_clase.reset_index()
print(df_sob_por_clase)

# Cambio los nombre de las columnas
df_sob_por_clase.columns = ['Clase', 'Sobrevivientes']
print(df_sob_por_clase)

# Crear grafico
plt.figure(figsize=(10,6),)
plt.bar(df_sob_por_clase['Clase'],df_sob_por_clase['Sobrevivientes'], color=['red','blue','green'])

# Etiquetas en el eje X
plt.xticks([1,2,3])

# Titulos de ejes
plt.title('Sobrevivientes del titanic por clase')
plt.xlabel('Clases')
plt.ylabel('Sobrevivientes')

plt.show()