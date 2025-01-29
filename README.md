CARACTERISTICAS:
Manejo de excepciones: Evita fallos por division entre cero o tipos de datos incorrectos.
Logging: Registra errores en un archivo errores.log.
Depuracion con PDB: Permite analizar el codigo en tiempo real.
Pruebas unitarias: Verifica que las operaciones funcionan correctamente.

EXPLICACION DEL CODIGO:
1.- MANEJO DE EXCEPCIONES
- Se maneja ZeroDivisionError en la función dividir().
- Se maneja ValueError si el usuario ingresa algo que no sea un número.
2.- LOGGING
- Registra errores en errores.log cuando hay división por cero o entrada incorrecta.
3.- DEPURACION CON PDB
- Si el usuario intenta dividir por 0, se activa pdb.set_trace(), permitiendo inspeccionar las variables en tiempo real.
El depurador pdb te permite inspeccionar y analizar el estado del programa en ese punto. Puedes probar los siguientes comandos en la consola donde aparece (Pdb):

Comandos útiles en pdb:
Comando	  Descripción
p b	      Muestra el valor de b (debería ser 0).
p a	      Muestra el valor de a.
n	        Ejecuta la siguiente línea de código.
s	        Entra dentro de la función dividir().
q     	  Sale del depurador y finaliza la ejecución del programa.

CONCLUSION:
Esta calculadora es tolerante a fallos porque:
- Evita caídas inesperadas gracias al manejo de errores.
- Registra errores para análisis posterior.
- Permite depuración en vivo si hay un problema crítico.
- Garantiza funcionamiento correcto con pruebas unitarias.
