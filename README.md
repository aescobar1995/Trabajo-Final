# Trabajo-Final

## AESeries

Este sitio se trata de una web tipo catalogo sobre Series de TV en esencia; a su vez va a contener una lista de Bingers afiliados, así como también Críticos especializados.

Se le llama Binger a las personas excesivamente clavadas con una, otra o varias series de televisión que pueden echarse hasta 23 episodios seguidos de su show favorito sin pararse más que para ir al baño.

Para el acceso va a tener dos tipos de usuarios, el usuario admin con permisos de Lectura, Escritura y Actualización en el sitio web. El otro es un usuario con solo permiso de lectura.

# Instalación 

Para la instalacion de este sitio debera hacer lo siguiente:

## Chequeo de la version de python:
Este proyecto fue escrito con python 3.10.4 por lo que le sugiero que pruebe con esta versión o una superior para no tener problemas de compatibilidad.

Para chequear la version de python: 

En *nix:

```bash
> python3 --version 
> Python 3.10.4
```

En windows:

```bash
c:\> py --version
c:\> Python 3.10.4
```
## Install Dependencies

Para instalar las dependencias necesitas ejecutar `pip install`, asegúrate de que estás en la carpeta del proyecto y puedes ver el archivo `requirements.txt` cuando hagas un `ls` o `dir`:

```bash
> pip install -r requirements.txt
```
Esto último devolverá las instalaciones requeridas.

`Algunos sistemas operativos le exigirán que utilice pip3 en lugar de pip `

## Configuración de la aplicación Django

Una vez que termines la instalación de las dependencias necesitas ejecutar algunos comandos de django.

### Migraciones

Iniciar la base de datos
*nix:
```bash
> python3 mananage.py migrate
```
windows:
```bash
c:\> py mananage.py migrate
```

### Correr el server

```bash
> python3 manage.py runserver
```
windows:
```bash
c:\> py manage.py runserver
```
Abrir un browser y escribir: localhost:8000/

y debera tener acceso a la pagina principal.

# Datos de base de datos

La Base de datos está conformada por:

# Tabla de **Serie**

|     |     |
| --- | --- |
| codserie | codigo o alias referente a la serie |
| nombre | nombre publicado |
| tipo | podría considerarse tambien como el genero |
| plataforma | Servicio de Streaming donde se encuentra la serie |
| fecha | fecha de emision de la temporada |
| episodios | cantidad de episodios de la temporada |
| temporada | numero de temporada |
| terminada | Si está o no terminada. |
| sinopsis | Esto es un pequeño resumen de la serie o temporada |
| imagen | Campo para agregar una imagen referencial |

# Tabla de **Critico**

|     |     |
| --- | --- |
| nombre | nombre del critico |
| apellido | apellido |
| email | email |
| alias | alias o seudónimo |
| experiencia | experiencia o estudios |

# Tabla de **Binger**

|     |     |
| --- | --- |
| nombre | nombre |
| apellido | apellido |
| email | email |
| alias | alias o seudónimo |

# Tabla de **Usuarios administradores y de lectura**

Para los accesos está registrado únicamente un admin y puede registrar tantos usuarios (solo lectura) que desee.

|     |     |
| --- | --- |
| **admin** | AESeries.123 |
| **usuario1** | AESeries.user1 |
| **usuario2** | AESeries.user2 |

# Para la administracion:
http://127.0.0.1:8000/admin/