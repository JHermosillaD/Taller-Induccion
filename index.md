# Taller de inducción "Análisis de datos básico"

## Resúmen general

<p style="text-align:justify">El taller se impartió por el Dr. Irving Morales, ex-estudiante de la facultad de Física. Se exploraron fuentes de datos abiertos, los principales formatos de datos que existen y los lenguajes de programación y herramientas necesarias para procesar y analizar los datos. Durante el taller no solo se presentaron las bases sobre el análisis de datos, ya que también se compartió su experiencia profesional y se resolvieron las dudas frente al mercado laboral como científico de datos. El taller incluyó sesiones prácticas en donde se realizaron análisis sobre los datos recolectados en la Encuesta sobre la percepción pública de la ciencia y la tecnología en México 2017 (ENPECyT) realizada por el INEGI.</p> 

> El Dr. Morales (@irvingfisica) ha creado un repositorio llamado enpecyt que concentra la documentación, los datos y la libreta en Jupyter del taller que impartió.

**Lista de reproducción del taller** <br>
[![IMAGE ALT TEXT HERE](/graficas/playlist.png)](https://www.youtube.com/playlist?list=PLZGw-MRdGtkFSRkboqz6dEbbpOl_hRCsX) 


### ¿Qué fuentes de datos abiertos existen en México?

<p>En México existen diferentes sitios que ofrecen sets de datos para su libre descarga. En general, los datos se dividen en categorías y se presentan en distintos formatos. Destacan tres sitios, incluido aquel que se consultó durante el taller:</p>

*   [Datos Abiertos de México](https://datos.gob.mx/)
*   [Portal de datos de la Ciudad de México](https://datos.cdmx.gob.mx/pages/home/)
*   [Instituto Nacional de Estadística y Geografía](https://www.inegi.org.mx/)<br>
        <img src="https://rde.inegi.org.mx/wp-content/uploads/2019/12/INEGI_a.png" width="250" height="50" />

## Requisitos

<p>El análisis se realizó en Jupyter, por lo que se usaron las librerías pandas y numpy para la manipulación de dataframes. Mientras que para la representación gráfica se usó la librería bokeh.</p>

### Ejemplo de gráficas con Bokeh realizados durante el taller

<p>Gráfica de tres círculos con diferente radio y color.</p>
<iframe src="circulos.html"
    sandbox="allow-same-origin allow-scripts"
    width="100%"
    height="520"
    scrolling="no"
    seamless="seamless"
    frameborder="0">
</iframe>

<p>Distribución de las calificacciones otorgadas por las personas a la respetabilidad del desempeño de los investigadores, donde donde 10 equivale a “Muy respetable” y 11 indica que no se sabe.</p>
<iframe src="graficas/barra.html"
    sandbox="allow-same-origin allow-scripts"
    width="100%"
    height="420"
    scrolling="no"
    seamless="seamless"
    frameborder="0">
</iframe>

## Análisis

### Análisis de datos
<p style="text-align:justify">Aquí se plantea estudiar las siguientes cuestiones ¿Los jóvenes interesados en ciencia tienen mejores posibilidades de conseguir empleo?, respecto a los gastos que hace el gobierno en apoyos a la invesetigación cientifíca, dígame si ¿cree que se está asignando o invirtiendo muy poco dinero, el monto correcto o demasiado dinero?. En el primer caso entre las respuestas posibles se encuentran las opciones 1:Muy de acuerdo,2 :De acuerdo, 3:En desacuerdo, 4:Muy en desacuerdo, 5:No sabe. En el segundo caso las respuestas posibles son 1:Muy poco, 2:Monto correcto, 3:Demasiado, 4:No sabe. Se filtró la base de datos por grado académico, luego se obtuvo un conjunto donde se buscó la primer pregunta y otro para la segunda.</p>

### Creación de gráficos

<p>Se muestran los porcentajes de las opiniones de las personas segun su grado académico. Se nota que la tendencia en la mayoría de los grados académicos es estar de acuerdo con que los jóvenes interesados en ciencia tienen mejores posibilidades de conseguir empleo.</p>
Las gráficas de la pregunta 27 inciso 1:
<iframe src="P27_1.html"
    sandbox="allow-same-origin allow-scripts"
    width="100%"
    height="350"
    scrolling="no"
    seamless="seamless"
    frameborder="0">
</iframe>
<p style="text-align:justify">Se puede ver un comportamiento diferente en las personas con Especialidad pues un 40% de ellos está en desacuerdo con dicha aclamación. También se observa que el 100% de las personas cuyo último grado de estudios fue preescolar se encuentran en desacuerdo con esa pregunta. Lo anterior es difícil de interpretar pues solo hubo un registro de ese grado académico.</p>
Las gráficas de la pregunta 28 inciso 4:
<iframe src="P28_4.html"
    sandbox="allow-same-origin allow-scripts"
    width="100%"
    height="350"
    scrolling="no"
    seamless="seamless"
    frameborder="0">
</iframe>

