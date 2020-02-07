# Mutantes

---API---

CNAME para probar la API:

    mutant end-point:

        Metodo: POST
        Url: django-env.3cphvmfxqh.us-west-2.elasticbeanstalk.com/mutant/
        Body ejemplo : { "dna":["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"] } 
    
    stats end-pont:
    
        Metodo POST
        Url: django-env.3cphvmfxqh.us-west-2.elasticbeanstalk.com/stats

---Requisitos---

Tener instalado:

    -python3.6/3.7
    -pip
    -virtualenv

---Correr Localmente---

La primera vez deberas realizar los siguientes pasos(en el mismo directorio donde se clono el repo):

    1. Crear el venv:
        python3 -m venv name-env

    2. Installar las dependencias:
        source name-env/bin/activate 
        pip install -r Mutants/requirements.txt
        python Mutants/manage.py makemigrations code
        python Mutants/manage.py migrate

con esto deberia estar todo instalado de forma tal de que el venv ya esta en condiciones de ejecutar el servidor de la API.

---Ejecutar localmente la API---

Pasos a seguir:

    1. activar venv (ejecutar parado en la carpeta donde se encuenta name-env y Mutants):
        source name-env/bin/activate 

    2. ejecutar el servidor (ejecutar parado en la carpeta Mutants):
        python manage.py runserver
        
---Actualizar la API---

Si se realiza alguna modificacion sobre el modelo ejecutar:

    python manage.py makemigrations

    python manege.py migrate

---Ejecutar Test----

    python manage.py test

---Code Coverage---
Para ver el code coverage del codigo ejectuar(en el directorio donde se encuentra manage.py):

    coverage run --source='.' manage.py test
    
    coverage report