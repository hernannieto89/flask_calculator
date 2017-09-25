# flask_calculator

Calculadora de operaciones aritmeticas con funcionalidad de persistencia
de sesiones en base de datos.

## Instalación
Requerimientos de base:
- [Python 2.7 +](https://www.python.org/)
- [PIP](https://pip.pypa.io/en/stable/quickstart/)
- [VirtualEnv](https://virtualenv.pypa.io/en/stable/)

Procedimiento:
```
$ git clone https://github.com/hernannieto89/flask_calculator
$ cd flask_calculator
$ virtualenv NOMBREENV
$ pip install -r requirements.txt
$ python manage.py createdb
$ python manage.py runserver
```

## Utilización

### Agregar operacion:
- URL: localhost:5000/operations
- METODO: POST
- PARAMETRO: input (String)

Importante: Si se utiliza logaritmo se debe introducir el argumento de dicha
función entre paréntesis, ie, log(5).

Si la operación es válida, se agrega a la sesión temporal.

### Listar operaciones
- URL: localhost:5000/operations
- METODO: GET

Lista las operaciones de la sesión temporal.
De no haber ninguna, devuelve una lista vacía.

### Limpiar operaciones
- URL: localhost:5000/operations
- METODO: DELETE

Limpia la lista de operaciones de la sesión temporal.

### Listar sesiones
- URL: localhost:5000/sessions
- METODO: GET

Lista las sesiones guardadas en la base de datos.
De no haber ninguna, devuelve una lista vacía.

### Guardar sesion
- URL: localhost:5000/sessions/NOMBRESESION
- METODO: POST
- PARAMETRO: session_name (String)

Guarda la sesión actual en la base de datos, siempre y cuanto tenga operaciones.
Si el nombre ya existe aborta la operación.
(Esto se deberia mejorar en el futuro)

### Obtener sesion
- URL: localhost:5000/sessions/NOMBRESESION
- METODO: GET

Busca una sesión y lista sus operaciones.
Esto no altera las operaciones de la sesion temporal.
Si la sesión no existe aborta la operación.

### Eliminar sesion
- URL: localhost:5000/sessions/NOMBRESESION
- METODO: DELETE

Elimina una sesión.
Si la sesión no existe aborta la operacion.

## Argumentos adicionales

- clean -> python manage.py clean

Limpia los archivos .pyc del directorio.

- show-urls -> python manage.py show-urls

Lista las reglas de URL con su respectivo ENDPOINT.
