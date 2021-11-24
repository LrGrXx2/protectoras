# protectoras
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
