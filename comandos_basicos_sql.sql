/*SELECT * FROM movements; seleccionar todos los registros de una tabla*/
/*SELECT concept,cuantity FROM movements; seleccionar algunos registros de una tabla*/
/* Insertar nuevos registros de la entidad o tabla movements
INSERT INTO movements(date,concept,cuantity)VALUES("2025-06-05","Comida",-150);*/
/* SELECT con WHERE
SELECT date,concept,cuantity FROM movements WHERE cuantity > 1000;*/
/* Modificar algún registro de la tabla 
UPDATE movements set concept= "desayuno", cuantity= -50 WHERE id=2;*/
/*Borrar registros de una tabla
DELETE FROM movements WHERE id = 3;*/
/*mostrar y ordenar con la condición que queramos
SELECT * FROM movements WHERE cuantity <0 ORDER BY date DESC, cuantity ASC;*/

