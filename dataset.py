import dask.dataframe as dd

#Paso2. Cargar lkos datos del dataset para procesamiento en paralelo
datos=dd.read_csv("student_depression_dataset.csv")
#Paso3. Filtrar lso registros de los estudiante mayores a 25 años
datosFiltrados=datos[datos["Age"]>25]
#Paso 4. Caculo estadistico 
estadistica=datosFiltrados.describe().compute()
print("registros filtrados")
print(estadistica)
