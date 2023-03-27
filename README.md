# nw-challenge
solucion desafio de selección

Para reproducir los resultados es necesario instalar poetry y tras clonar el repositorio ejecutar 
```
$poetry install
```
# MODELS
Este directorio posee un notebook donde se testean diferentes modelos de clasificacion con distintos hiperparametros,
todos sus resultados se encuentran registrados mediante el uso de W&B.

# CW-API 
Contiene la api solicitada para la prediccion, para usarla se debe activar el entorno y ejecutarla con
```
$uvicorn xgb-api:app --reload 
```
una vez ejecutada, enviar el post a la direccion entregada para uso local.



