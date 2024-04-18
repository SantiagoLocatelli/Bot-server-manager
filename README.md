# Setting up our environment

**THIS IS TRULY IMPORTANT**
We must be using python 3.10.6
Too check wich version of python we have we can use the command *python --version*

## This is for linux
python3 -m venv env

source env/bin/activate

**IMPORTANT**
Before we install our requirements we must add this dependency
- psycopg2-binary==2.9.3

pip install -r requirements.txt

## This is for windows

You need to know that if you are using git bash this following commands won't be useful, you must use the commands above

Once you have installed python you must install pip and we get that with the next 2 commands:
- curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
- python get-pip.py

And now we set up our application environment
- python -m venv env
- env\Scripts\activate or .\env\Scripts\activate

**IMPORTANT**
Before we install our requirements we must add this dependency
- psycopg2==2.9.6

pip install -r requirements.txt

# We must install docker

- windows: [link](https://docs.docker.com/desktop/install/windows-install/)
- linux: [link](https://phoenixnap.com/kb/install-docker-on-ubuntu-20-04)

## Useful commands:

- build: docker-compose build
- get up: docker-compose up -d
- build and up: docker-compose -f docker-compose.yml up -d --build
- turn down: docker-compose down

# Connect to local postgres db

## First of all we must install postgresql

- windows: [link](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
- linux: sudo apt-get install postgresql

## Local
### For linux
psql -p 5434 -U postgres -h 0.0.0.0

### [For windows](https://stackoverflow.com/questions/56993263/connect-to-dockerized-postgres-from-windows-docker-host)


## Remote 
PGPASSWORD=0aFeWQNYnsFSpYDeaW9jwpDhxKfQXRC2 psql -h dpg-chsk4uhmbg57s5r5m1d0-a.oregon-postgres.render.com -U support pensamiento_computacional


# BOTARDO

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

MTEyODg3MDk2ODMzNzYzNzM3Nw.GBtw50.I0mUSPpF-d_-p7gHEjqp4FQpl-_EXXNYVWeEiE

ogFDaedBk2hEJIV2aWnBZ1bZtZUPZC7a

https://discord.com/oauth2/authorize?client_id=1128870968337637377&scope=bot&permissions=8


sudo apt install mysql-client-core-8.0
sudo apt install mariadb-server
mysql -h db-fde-02.sparkedhost.us -u u101170_FUwsSHLLAZ -p
8ABhJk7uTxsig9Bo.1S!adG3
use s101170_PensamientoComputacional;


insert into alumno (cuit, nombre, cuatrimestre_id, registrado, estado, discord_id) values ('42930636', 'OJEDA ABRIL', 1, 0, 1, NULL);


export FLASK_APP=project/__init__.py &&  python3 manage.py run

##### obtener alumnos repetidos
select cuit from alumno group by cuit having count(*) > 1;


# como esta estructurado el proyecto?

Se resume en dos programas. Uno es el bot y el otro es la API. La idea es que el bot reciba los comandos de los alumnos y le vaya pegando a la API a medida que se necesite. Es la API quien se comunica con la base de datos, quien realmente da de baja o de alta a un alumno, el bot delega este comportamiento a la API.

# Que hacer a penas descargamos el repositorio?

## API

En un bash, parados en la raiz del proyecto, tiramos el siguiente comando para crear el virtual environment de python 
```
python3 -m venv api_venv
```

Una vez creado tenemos que activar el venv, lo hacemos con el comando 
```
source api_venv/bin/activate
```

Una vez activado tenemos que instalar todas las dependencias
```
pip install -r requirements.txt
```

Una vez hecho todo eso ya estamos en condiciones de levantar la API.

## BOT

Es un proceso muy similar. No paramos dentro de la carpeta bot y en un bash ejecutamos.
```
python3 -m venv bot_venv
source bot_venv/bin/activate
pip install -r requirements.txt
```

Una vez ejecutado todos esos comandos estamos en condiciones de correr el BOT localmente.

# Como correr la API localmente?

Si estas el VS Code es muy facil, en la carpeta .vscode ya esta configurado el archivo launch.json para poder levantar la api simplemente desde la seccion Run and Debug del VS Code.


Para levantar la API directamente desde el bash podemos hacer:
```
source api_venv/bin/activate
FLASK_APP="project/__init__.py"
python3 manage.py run
```

# Como correr el BOT localmente?

Para levantar el BOT directamente desde el bash podemos hacer:
```
source bot_venv/bin/activate
python3 main.py
```

# Como nos conectamos a la db?

Yo tuve que instalar algunas dependencias primero
```
sudo apt install mysql-client-core-8.0
sudo apt install mariadb-server
```

Para entrar a la db:
```
mysql -h db-fde-02.sparkedhost.us -u u101170_FUwsSHLLAZ -p
```

Nos va a pedir una contraseña
```
8ABhJk7uTxsig9Bo.1S!adG3
```

Y nos tenemos que cambiar de schema, lo hacemos
```
use s101170_PensamientoComputacional;
```

Y ahi ya estamos listos para hacer consultas, insertar, etc.

# Como insertar una nueva lista de alumnos de un nuevo cuatri?

Primero que nada, hay que insertar un nuevo cuatrimestre en la tabla de cuatrimestre, lo hacemos:
```
insert into cuatrimestre (description) ('2024 1C');
```

Luego, hay que agregar el archivo csv de los alumnos en la carpeta correspondiente dentro de la carpeta db. Es importante que el archivo csv mantenga la misma estructura que los otros archivos, usarlos como guia.

Una vez agregado este archivo, lo que se tiene que hacer es levantar la API localmente y ejecutar el endpoint que tiene la terminacion '/v1/students' y de tipo POST, el cual el body tiene dos parametros:
- filename: es el path relativo en el que se encuentra el archivo con los alumnos, por ejemplo, project/db/2024 1C/inscriptos 2024 1C.csv
- cuatrimestre: el id de cuatrimestre en el cual se quieren insertar los alumnos, este id es el que se genera en el primer paso.

Una vez ejecutado todo esto correctamente ya se van encontrar los alumnos en la DB.