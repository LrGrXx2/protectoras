# Protectoras+
Web con base de datos que recopila información de varias protectoras aragonesas.
Consta de tres clases (Protectora, Animal y Rescate) con sus respectivos elementos.
La clase Rescate tinene dos llaves foráneas, una de Protectora y otra de Animal,
de esta forma quedan unidas las tres tablas.

- PROTECTORA: nombre_protectora, direccion, ciudad, coordenadas                              
- ANIMAL: especie, nombre_raza, descripcion_animal
- RESCATE: nombre_animal, adoptado (booleano), descripcion_rescate, *nombre_protectora, *especie
 
En la página principal vemos un menú desplegable funcional, debajo un mapa en el que se van poniendo
los puntos de las protectoras automáticamente al crear la Protectora, este mapa podemos aumentarlo, 
disminuirlo y movernos por el. Abajo del todo está un buscador de Rescates.


¿Cómo lo instalo y hago funcionar?
1. nos posicionamos donde queramos tener la capeta en la cmd (con cd)
2. copiamos el enlace del repositorio git donde está el trabajo
3. en la cmd escribimos: git clone https://github.com/LrGrXx2/protectoras.git (enlace del repo)
4. nos posicionamos dentro del proyecto en la cmd (con cd)
5. creamos entorno virtual (py -m venv env)
6. activamos el entorno virtual (env\Scripts\activate.bat)
7. dentro del entorno instalamos Django (py -m pip install Django)
8. dentro del entorno instamos debugtoolbar (pip install dejango-debug-toolbar)
10. py manage.py runserver (para cerrarlo: Ctrl + c)
