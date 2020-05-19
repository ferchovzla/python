El covid19_analysis, se refiera a un ejercicio basado en el artículo [Explorando datos del Covid19 con pandas](https://www.seraph.to/python-pandas-covid19-1.html#python-pandas-covid19-1)

En el ejercicio se analizan los casos diarios de **Covid-19** a nivel mundial y se realizan comparativas entre diferentes países latinoamericanos, mostrando las tendencias y curvas correspondientes. Los datos utilizados provienen del repositorio del [COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19)

Para acceder a los datos se debe clonar el repositorio de manera local:

```$>git clone https://github.com/CSSEGISandData/COVID-19.git```

Para actualizar el repositorio, debes hacer lo siguiente:

```
   $>cd COVID-19
   $>git pull origin master

```

Se utilizan las librerías:
* **pandas** para el analisis de los datos.
* **datetime** para el manejo de las fechas.
* **pathlib** para manejar las rutas de archivos csv en el sistema.
* **matplotlib.pyplot** para representar en los gráficos el comportamiento de la enfermedad.


 ![Tabla de tasa de contagiados en Perú](https://ibb.co/423LLh7)

 ![Gráfico comparativo de número de contagiados en Colombia. Chile, Ecuador, Perú y Chile](https://ibb.co/q0j68rF)

 ![Gráfico comparativo de tasa de contagios diarios en Colombia. Chile, Ecuador, Perú y Chile](https://ibb.co/nRq57J8)

 ![Gráfico comparativo de muertes por Covid-19 en Colombia. Chile, Ecuador, Perú y Chile](https://ibb.co/gJLnk6k)
