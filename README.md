# nw-challenge
solución desafío de selección

Para reproducir los resultados es necesario instalar poetry y tras clonar el repositorio ejecutar 
```
$poetry install
```
# MODEL
Este directorio posee un notebook donde se testean diferentes modelos de clasificación con distintos hiperparametros,
todos sus resultados se encuentran registrados mediante el uso de W&B. Las conclusiones respecto a estos experimentos
se encuentran en el notebook de model-testing.

# CW-API 
Contiene la api solicitada para la prediccion, para usarla se debe activar el entorno y ejecutarla con
```
$uvicorn xgb-api:app --reload 
```
una vez ejecutada, enviar el post a la direccion entregada para obtener la predicción.


# DEPLOY API
Para hospedar la api, se hizo uso de heroku. El enlace a la api es: https://git.heroku.com/limitless-castle-66721.git.
Para Build y Deploy de la api, se hizo uso de Servicios Cloud de Google, el cual cuenta con una sencilla forma de implementar
estas funciones.

# Benchmarking_Tool_Results
En la imagen benchmark_results.png se pueden ver los resultados para la prueba de estres realizada sobre la api.
Para mejorar los resultados la prueba de rendimiento debe llevarse a cabo a lo largo del ciclo de vida de la aplicación para abordar los problemas que podrían surgir una vez que la aplicación entre en funcionamiento, cuando aumente la base de usuarios o cuando se modifique la funcionalidad de ciertas características críticas.
El PT debe llevarse a cabo durante varias iteraciones para obtener los mejores resultados. Esto requiere mucho tiempo y dinero según el tipo de aplicación y un conjunto particular de API para lograr el rendimiento deseado con una configuración de recursos optimizada.
