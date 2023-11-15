# Instalacción del proyecto

Este proyecto fue realizado en una maquina Windows utilizando Windows Subsystem for Linux (wsl)

en la mayoria del codigo no afecta, unicamente en el formato de como se escriben las rutas (para tomarlo en cuenta)

En caso de no utilizar wsl se requiere de realizar cambios en las rutas de documentos 
(actualmente solo se encontraria el problema en el modulo /gen_report/views.py - line 79)

---

Primero para ejecutar la aplicación es necesario crear un entorno virtual con virtualenv

```shell
# Instalación de virtualenv
pip install virtualenv[20.24.6]

# Creación del entorno
virtualenv [nombre-del-entorno]
virtualenv env

# Activando el entorno 
env\Scripts\activate # Windows

source tutorial-env/bin/activate # Linux o WSL
```

Teniendo activado el entorno se requiere de instalar las dependencias, las cuales se encuentran en el documento de `requeriments.txt`

```shell
# Instalando las dependencias
pip install -r requeriments.txt
```

Hasta este punto la aplicación debe funcionar, para ejecutar el programa se requiere introducir la siguiente instrucción

```shell
py manage.py runserver # Windows
python3 manage.py runserver # Linux o WSL
```