Detalles de alcance
============================

### Panel principal.
La interfaz de usuario consultará, por medio de una consola, si se desea hacer un análisis de video o visualizar un reporte. Si se selecciona la primera, se mostrará los mensajes de solicitud de video. De lo contrario se visualizarán los posibles reportes a consultar.

### Obtener frames de video.
Los frames podrán obtenerse de un archivo de vídeo (formatos por definir) o de una cámara IP. Al utilizar cualquiera de las dos fuentes mencionadas, se abrirá una ventana con el contenido del video.

### Análisis.
El análisis en tiempo real del video permitirá leer las placas de los vehiculos, identificar si es infractor de tránsito y almacenar la información (placa, IP de la cámara o nombre del video, fecha, hora y si es infractor o no). Para almacenar estos datos, se utilizará SQLite.

### Reportes. (herramientas por definir)
- **Tabla o gráfico de cantidad de autos infractores por fuente de vídeo**.
- **Tabla o gráfico de cantidad de autos infractores por fecha y hora**.