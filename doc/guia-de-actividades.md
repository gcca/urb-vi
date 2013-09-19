Ciclo de tareas
===============

### Ciclo básico

1. Definir tarea
2. Documentar conocimiento necesario de la tarea[^1]
3. Desarrollar
4. Escribir pruebas
5. Generar *patch*
6. Enviar para integrar[^2]

[^1]: Acerca de la API, teoría o biblioteca de desarrollo. Ubicar en un `*.md` o como comentario dentro del código.

[^2]: Para evitar conflictos, después de este ciclo, el resto debe actualizar su rama local.



### Glosario

- **Describir**: Especificación por UML, Lepus3, texto. Detallar interfaz de software.
- **Imp.**: Importancia.
- **Est.**: Estimación.
- **Detección**: Ubicar con una coordenada *(x, y)* la posición del objeto.
- **Segementacion**: Identificar y ubicar las partes del objeto. En el caso de los autos: saber dónde se encuentra la placa, la llanta, el parabrisas.
- **Reconocimiento**: Fase final como leer placa, contar autos, identificar persona, etc.
- **Esqueleto**, de la aplicación: Por ejemplo, en ArgoUML se puede generar código a partir del modelo; eso es el esqueleto. Es decir, la *__declaración__* de cada clase y sus métodos y las relaciones entre ellos, en *__código__*.



### Principales requisitos
1. Estructurar repositorio
2. Crear documentación inicial
3. Diagrama de módulos
4. IU de línea-de-comandos
5. Almacenamiento de datos -- *sqlite3*
6. Captura de imagen -- HTTP, video
7. Procesar imagen: detección, segmentación, extracción de características
8. Interfaces entre módulos -- Ing.Soft.
9. Identificar infractores -- Consulta web
10. Densidad de infractores
11. Integración y empaquetado

> **NOTA**: *Ruta de infractores* (Por verse...)



### Pila

 N | Nombre                                        |Imp.|Est.
:-:|-----------------------------------------------|:--:|:--:
 1 | Estructurar repositorio                       |  5 |  5
 2 | Crear documentación inicial                   |  7 |  3
 3 | Diagrama de módulos                           |  8 |  5
 4 | IU de línea-de-comandos                       |  4 |  5
 5 | Almacenamiento de datos                       |  3 |  6
 6 | Captura de imagen                             |  7 |  8
 7 | Procesar imagen                               | 10 | 10
 8 | Interfaces entre módulos                      | 10 |  7
 9 | Identificar infractores                       |  4 |  5
10 | Densidad de infractores                       |  2 |  8
11 | Integración y empaquetado                     |  6 |  5



### Detalle
Las tareas están numeradas y las notas que pueden ayudar en la tarea están con viñetas.

> **NOTA**: Considerar el método más sencillo, aun si involucra un margen de error mayor.

1. Estructurar repositorio
	1. Crear repositorio
	2. Distribuir módulos (básico)
2. Crear documentación inicial
	1. Manuales de uso de bzr, editores
	2. Estándares de programación (posible uso de *pylint*)
	3. Gestión de tareas
3. Diagrama de módulos
	1. Diagrama de componentes
	2. Diagrama de clases o Lepus3
4. IU de línea-de-comandos
	1. Definir esquema de opciones básicas
		- ayuda
		- descripción de la aplicación
	2. Definir interfaz de programación
	3. Segmentar por módulos (cada módulo define su conjunto de opciones) (ver esquema de *nose*)
5. Almacenamiento de datos -- *sqlite3*
	1. Definir modelo de datos
	2. Definir interfaz de programación
	3. Especificación, restricciones y pruebas unitarias
	4. Verificar cosas como
		- rutas relativas
		- fichero de base de datos vacío
		- inexistente
		- mal-formado
6. Captura de imagen -- HTTP, video
	1. Averiguar mecanismos para obtener el video desde la cámara
	2. Averiguar como capturar las imágenes
	3. Evaluar posibles complicaciones
		- latencia
		- frecuencia de transmisión
		- retrasos (*delays*)
		- formato de imagen
7. Procesar imagen: detección, segmentación, extracción de características
	1. Obtención de imagen
		- Filtros de imagen
		- Correciones pos calidad
		- Formato de imagen
	2. Detección de auto
		- Mecanismos de detección
		- Flujo
		- Bordes
		- Haarcascade
		- Diferencia de fondo
	3. Segmentación de auto -> Buscar posición de placa
		- Identificar calidades de placa
		- Identificar problemas de perspectivas.
		- Calidad de la imagen para la lectura
	4. Reconocimiento de placa (lectura)
		- Métodos de lectura (Tesseract)
		- Considerar si las herramientas contemplan partes de los procesos previos (para reducir esfuerzo).
		- Margen de error en la lectura (margen total, dado la eficiencia de los procesos previos)
8. Interfaces entre módulos -- Ing.Soft.
	1. Diagrama para dependencias (Lepus3 o UML)
	2. Detallar flujo del programa (workflow)
	3. Escribir esqueleto de la aplicación
9. Identificar infractores -- Consulta web
	1. Averiguar la web de infracciones
	2. Identificar estructura de extracción (scraping / scrawling) (posible uso de *scrapy*)
	3. Definir interfaz y escribir módulo (Ver posibles libs: scrawpy, curl, urllib[12], socket ;))
10. Densidad de infractores
	1. Crear grafo en base a los dispositivos
	2. Identificar los dispositivos con más infractores
11. Integración y empaquetado
	1. Generar un ejecutable único (de ser posible) o ver distribución de binarios



### Acerca del modelo de datos
El modelo de datos debe contemplar lo necesario para poder implementar los casos de uso. Por ejemplo, para la densidad, debe guardar posición geográfica o dirección.



Iteraciones
===========

Primera Iteración: *Las demos*
------------------------------

### Análisis de dependencia
 N | Componente                       | Aporte
:-:|----------------------------------|:------:
 1 | Interfaz de Línea de comandos    | 3
 2 | Persistencia y lógica de datos   | 3  1
 3 | Esqueleto de la aplicación       |
 4 | Obtención de la imagen           | 3
 5 | Detección de autos               | 3  4
 6 | Segmentación de auto             | 3  5
 7 | Reconocimiento de placa          | 3  6

> **NOTA**: 4-7 no dependen de los anteriores, porque el resultado será impreso en la consola, durante esta iteración.



### Análisis de precisión
 N | Componente                   | Precisión | Aporte
:-:|------------------------------|:---------:|:------:
 1 | Sistema global               |    50%    |
 2 | Obtención de la imagen       |    55%    |    5%
 3 | Detección de autos           |    80%    |   25%
 4 | Segmentación de auto         |    95%    |   15%
 5 | Reconocimiento de placa      |   100%    |    5%

> **Sistema global**: Referido a la interfaz de usuario, persistencia de datos, etc. Lo que no es parte de la precisión de la lectura de placas.



### Hitos
1. Interfaz de línea de comandos suficiente para ejecutar la aplicación.
2. Esqueleto de la aplicación para completar las porciones de código.
3. Demo de obtención de video
	1. Línea de comando: demo/obtener.py [HTTP/FILE]
	2. Abrir ventana con el video
4. Demo detectar autos
	1. Línea de comando: demo/detectar.py [IMG]
	2. Abrir ventana con la imagen y los autos marcados.
5. Demo segmentar auto
	1. Línea de comando: demo/segmentar.py [IMG]
	2. Abrir ventana con la imagen de la placa marcada.
6. Demo reconocimiento de placa
	1. Línea de comando: demo/reconocer.py [IMG]
	2. Imprimir en consola la cadena de texto con la placa.

> **NOTA 1**: *Marcado* se refiere a encerrar en un círculo o cuadrado la zona de interés.

> **NOTA 2**: La lista no declara el orden de implementación. No es necesario programar según el número de la lista.

> **NOTA 3**: Cada hito debe estar acompañado de sus pruebas unitarias (o automatizadas), documentación del método, y margen de error (indicadores como: presición, exhaustividad, promedio, puntuación F1). (Referencia: [Wikipedia: Precisión y Exhaustividad]([http://es.wikipedia.org/wiki/Precisi%C3%B3n_y_exhaustividad))



### Alcance
*__Pasar el fichero de alcance aquí__*

### Estado

 Hito | Estado
:----:|----------
  1   | Hecho
  2   | Hecho
  3   | Hecho
  4   | Pospuesto
  5   | Hecho
  6   | Hecho