## Taller de inducción "Análisis de datos básico"

### Resúmen general

<p style="text-align:justify">El taller fue impartido por el *Dr. Irving Morales*, ex-estudiante de la facultad de Física. Durante el taller se presentó el estado actual del ecosistema de datos abiertos en México y algunas de las principales fuentes de información existentes en el país. Se habló de los distintos tipos de datos existentes, los principales formatos en los que se encuentran y las herramientas necesarias para procesarlos y analizarlos.<br> 
El taller incluyó sesiones prácticas en donde se realizaráó análisis sobre los datos recolectados en la Encuesta sobre la percepción pública de laciencia y la tecnología en México 2017 (ENPECyT) realizada   por   el   INEGI.</p>

[![IMAGE ALT TEXT HERE](https://i.ytimg.com/vi/xBbM3YuJi8Y/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLATfQMQnXT7CZi84whsntVxZNxbEw)](https://www.youtube.com/playlist?list=PLZGw-MRdGtkFSRkboqz6dEbbpOl_hRCsX)

### ¿Qué fuentes de datos abiertos existen en México?

<p>En México existen diferentes sitios que ofrecen sets de datos para su libre descarga. En general, los datos están divididos por categorias y ofrecen difentes formatos. Destacan tres sitios, incluido aquel que se consulto durante el taller:</p>

*   [Datos Abiertos de México](https://datos.gob.mx/)<br>
        <img src="https://www.gob.mx/cms/uploads/article/main_image/6308/politicadatos2-380x280.jpg" width="144" height="111" />
*   [Portal de datos de la Ciudad de México](https://datos.cdmx.gob.mx/pages/home/)<br>
        <img src="https://www.poderjudicialcdmx.gob.mx/unidadtransparencia/wp-content/uploads/datos-abiertos.jpg" width="160" height="104" />
*   [Instituto Nacional de Estadística y Geografía](https://www.inegi.org.mx/)<br>
        <img src="https://rde.inegi.org.mx/wp-content/uploads/2019/12/INEGI_a.png" width="250" height="50" />

## Requisitos

<p>El análisis se realizó en Jupyter, por lo  que se usó las librerías *pandas* y *numpy* para la maniulación de dataframes. Mientras que para la representación gráfica se usó la librería *bokeh*.</p>

### Ejemplo de Gráficos con Bokeh durante el taller

<p>Grafica de tres círculos con diferente radio y color</p>

<iframe src="circulos.html"
    sandbox="allow-same-origin allow-scripts"
    width="100%"
    height="500"
    scrolling="no"
    seamless="seamless"
    frameborder="0">
</iframe>

Distribución de las calificacciones otorgadas por las personas a la respetabilidad del desempeño de los investigadores, donde donde 10 equivale a “Muy respetable” y 11 indica que no se sabe. 

<iframe src="graficas/barra.html"
    sandbox="allow-same-origin allow-scripts"
    width="100%"
    height="500"
    scrolling="no"
    seamless="seamless"
    frameborder="0">
</iframe>

## Análisis de datos

# Análisis I
<p style="text-align:justify">Aquí se plantea estudiar las siguientes cuestiones ¿Los jóvenes interesados en ciencia tienen mejores posibilidades de conseguir empleo?, respecto a los gastos que hace el gobierno en apoyos a la invesetigación cientifíca, dígame si ¿cree que se está asignando o invirtiendo muy poco dinero, el monto correcto o demasiado dinero?. En el primer caso entre las respuestas posibles se encuentran las opciones 1:Muy de acuerdo,2 :De acuerdo, 3:En desacuerdo, 4:Muy en desacuerdo, 5:No sabe. En el segundo caso las respuestas posibles son 1:Muy poco, 2:Monto correcto, 3:Demasiado, 4:No sabe. Se filtró la base de datos por grado académico, luego se obtuvo un conjunto donde se buscó la primer pregunta y otro para la segunda.</p>

## Creación de gráficos

<p>Se muestran los porcentajes de las opiniones de las personas segun su grado académico. Se nota que la tendencia en la mayoría de los grados académicos es estar de acuerdo con que los jóvenes interesados en ciencia tienen mejores posibilidades de conseguir empleo.</p>
Las gráficas de la pregunta 27 inciso 1:
<iframe src="P27_1.html"
    sandbox="allow-same-origin allow-scripts"
    width="100%"
    height="500"
    scrolling="no"
    seamless="seamless"
    frameborder="0">
</iframe>
<p style="text-align:justify">Se puede ver un comportamiento diferente en las personas con Especialidad pues un 40% de ellos está en desacuerdo con dicha aclamación. También se observa que el 100% de las personas cuyo último grado de estudios fue preescolar se encuentran en desacuerdo con esa pregunta. Lo anterior es difícil de interpretar pues solo hubo un registro de ese grado académico.</p>

Las gráficas de la pregunta 28 inciso 4:
<iframe src="P28_4.html"
    sandbox="allow-same-origin allow-scripts"
    width="100%"
    height="500"
    scrolling="no"
    seamless="seamless"
    frameborder="0">
</iframe>

