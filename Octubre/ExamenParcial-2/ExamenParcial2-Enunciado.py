"""
-------------------- EXAMEN PARCIAL 2 --------------------

Desarrollar un programa que verifique si una placa ingresada por teclado, es válida dentro
del territorio nacional Boliviano.

Cada requerimiento/validación (puntos 1) al 3) tendrán un puntaje de 4 puntos, el Pull Request 3 puntos, total 15 puntos)

Deberá ser entregado dentro del Folder "ExamenParcial-2", mediante un Pull Request desde una rama (branch) con las iniciales de su nombre completo...
Ejemplo estudiante "Juan Pablo Perez Stauffenberg":  (branch/rama) >>>  JPPS-Parcial2  <<<<
El Pull Request NO debe ser mergeado al repositorio por el alumno, esto lo hará el Docente, el estudiante SÓLO debe crear el Pull Request.
El Pull request conlleva aplicar lo aprendido para el 2do parcial sobre:
- Versionamiento, buenas prácticas de versionamiento, comandos git, branches.

El código debe tener lo avanzado hasta el 2do parcial sobre código limpio y buenas prácticas de desarrollo:
- Variables con nombres descriptivos (se restará 1 punto si no lo aplica)
- Uso de llamadas a funciones/métodos. (se restará 1 punto si no lo aplica)
- Sintaxis. (se recomienda el uso)
- Mensajes de impresión descriptivos. (se restará 1 punto si no lo aplica)

REQUERIMIENTOS (validaciones)
1) Las placas bolivianas no deben sobrepasar 8 caracteres (entre números, letras y símbolos PERMITIDOS: espacio o guión)

ejemplos válidos de placas
444 ABC  #Placa Válida
123-ASE  #Placa Válida
A12-454  #Placa Inválida
2124-ABC #Placa Válida
4811 ABC #Placa Válida

2) Solo números pueden empezar una placa; las letras deben ir al final siempre.
   Deben tener AL MENOS 3 dígitos (números al iniciar), es decir el código debe validar lo que ingrese el usuario por teclado de la siguiente manera.
Ejemplos válidos: 123ABC, 1234XYZ, 8429-JVS, 428 EUX
Ejemplos inválidos: ABC123, A2XXYZ, 12-XYZ, 0AB-XYZ

3) No se debe permitir el uso de los siguientes caracteres en la placa: 
. (punto) 
@ (arroba)
# (numeral)
"""