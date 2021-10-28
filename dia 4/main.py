import numpy as np
import pandas as pd

#Leer el archivo 
df = pd.read_csv("insurance.csv")
print(df)

#Mostrar cantidad de variables y datos
df.describe()
df.info()

#Calcular promedio, media y moda de age
media_age = df["age"].mean()
mediana_age = df["age"].median()
moda_age = df["age"].mode()
desv_age = df["age"].std()
minimo_age = df["age"].min()
maximo_age = df["age"].max()

print("\n")
print("AGE")
print("Media: ",media_age)
print("Mediana: ",mediana_age)
print("Moda: ",moda_age)
print("Desviación Estándar: ",desv_age)
print("Minimo: ",minimo_age)
print("Máximo: ",maximo_age)

#Calcular promedio, media y moda de 
media_bmi = df["bmi"].mean()
mediana_bmi = df["bmi"].median()
moda_bmi = df["bmi"].mode()
desv_bmi = df["bmi"].std()
minimo_bmi = df["age"].min()
maximo_bmi = df["age"].max()

print("\n")
print("BMI")
print("Media: ",media_bmi)
print("Mediana: ",mediana_bmi)
print("Moda: ",moda_bmi)
print("Desviación Estándar: ",desv_bmi)
print("Minimo: ",minimo_bmi)
print("Máximo: ",maximo_bmi)

#Calcular promedio, media y moda de age
media_chi = df["children"].mean()
mediana_chi = df["children"].median()
moda_chi = df["children"].mode()
desv_chi = df["children"].std()
minimo_chi = df["children"].min()
maximo_chi = df["children"].max()

print("\n")
print("CHILDREN")
print("Media: ",media_chi)
print("Mediana: ",mediana_chi)
print("Moda: ",moda_chi)
print("Desviación Estándar: ",desv_chi)
print("Minimo: ",minimo_chi)
print("Máximo: ",maximo_chi)

#Calcular promedio, media y moda de age
media_char = df["charges"].mean()
mediana_char = df["charges"].median()
moda_char = df["charges"].mode()
desv_char = df["charges"].std()
minimo_char = df["charges"].min()
maximo_char = df["charges"].max()

print("\n")
print("CHARGES")
print("Media: ",media_char)
print("Mediana: ",mediana_char)
print("Moda: ",moda_char)
print("Desviación Estándar: ",desv_char)
print("Minimo: ",minimo_char)
print("Máximo: ",maximo_char)
