# Nombre del Proyecto

Descripción breve del proyecto.

## Instalación

Sigue estos pasos para instalar y configurar el proyecto en tu entorno local.

### Prerrequisitos

Antes de comenzar, asegúrate de tener instalado Python en tu sistema. Este proyecto fue desarrollado con Python 3.8, pero debería ser compatible con versiones posteriores.

### Configuración del entorno virtual

1. Abre una terminal en tu computadora.
2. Navega al directorio donde deseas colocar el proyecto.
3. Ejecuta el siguiente comando para crear un entorno virtual llamado `venv`:

python3 -m venv venv

4. Activa el entorno virtual:

- En Windows:

.\venv\Scripts\activate

- En macOS/Linux:

source venv/bin/activate

### Clonación del proyecto

Con el entorno virtual activado, clona el repositorio del proyecto dentro de un directorio `src` utilizando el siguiente comando:

mkdir src && cd src
git clone <URL_DEL_REPOSITORIO> .

Reemplaza `<URL_DEL_REPOSITORIO>` con la URL real del repositorio del proyecto.

### Instalación de dependencias

Una vez clonado el proyecto, instala las dependencias necesarias ejecutando:

pip install -r requirements.txt

Asegúrate de estar en el directorio raíz del proyecto (`src`) donde se encuentra el archivo `requirements.txt`.

