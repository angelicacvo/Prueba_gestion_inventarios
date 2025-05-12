**Caso de uso**

Sistema que permita gestionar el inventario de una tienda de manera dinámica, para que pueda realizar un seguimiento eficiente de los productos disponibles, su cantidad y precios actualizados, además de calcular el valor total del inventario.

**Desarrollo:** 

El programa interactúa con el usuario a través de la consola, solicitando datos como:

- nombre delproducto (name)
- precio del producto (price)
- cantidad del producto (quantity)
Este, a su vez tiene un menú intuitivo el cual permite que el usuario decida la opción que más se acomode a su necesidad.

**Requerimientos:**

- El programa debe permitir agregar al menos 5 productos iniciales.
- Al consultar un producto, debe indicar si no existe en el inventario con un mensaje claro.
- La actualización de precios debe validar que el nuevo precio sea un número positivo.
- La eliminación de un producto debe confirmar su existencia antes de borrarlo.
- El cálculo del valor total del inventario debe ser preciso y mostrar el resultado con dos
decimales.
- El código debe estar estructurado en funciones para cada operación y debe incluir
comentarios explicativos.
- El código y los comentarios deben estar 100% sin excepción alguna en inglés.

**Explicación del código:**

El código está dividido modularmente por funciones tanto como para agregar, eliminar, actualizar, entre otras, como para calcular valor total de los productos en el inventario según los productos ingresados en el sistema.
Funciones:

- validate_str(): Valida que el valor ingresado por el usuario sea un string vacío y que sea un valor alfanumérico.
- validate_num(): Valida que el valor ingresado por el usuario sea numerico y que sea un entero mayor a 0.
- add_product(): Busca en el sistema el producto, si existe manda un mensaje que el producto ya existe en la base de datos; si no existe lo agrega al diccionario inventory con su nombre, precio y cantidad respectivos. Valida que los datos ingresados sean válidos.
- get_product():  Busca en el sistema el producto, si no existe manda un mensaje que el producto no existe; si existe envía los datos pertenecientes al producto buscado. Valida que los datos ingresados sean válidos.
- update_product(): Busca en el sistema el producto, si no existe manda un mensaje que el producto no existe no existe; si existe le pide al usuario que ingrese el precio a cambiar. Valida que los datos ingresados sean válidos y manda un mensaje si la operación es exitosa.
- delete_product(): Busca en el sistema el producto, si no existe manda un mensaje que el producto no existe no existe; si existe le envía al usuario los datos pertenecientes a este producto y un mensaje de confirmación para eliminar el producto, si desea eliminarlo se elimina, si no se detiene la operación y le pide una nueva opción.
- calculate_inventory(): realiza una operación de multiplicación de los valores precio y cantidad de los productos en el inventario, retorna un valor con dos decimales.
- menu(): contiene las opciones del menú con el cual va a interactuar el usuario.
- Por medio de un match, case, se asigna a cada opción una función para que sea funcional, si el usuario ingresa una opción no válida se enviará un mensaje de: Opción no válida


**Ejemplos de entrada y salida del sistema:**

Bienvenido a tu inventario. Ingresa la opción que deseas realizar

  - [1] Agregar producto al inventario
  - [2] Consultar producto del inventario
  - [3] Actualizar precio del inventario
  - [4] Eliminar producto del inventario
  - [5] Calcular el valor total del inventario
  - [6] Salir del sistema de inventarios

**Opción 1**
Opción del usuario: 1 (Agregar producto)

Ingresa el nombre del producto: 

Opción del usuario: Pan

Ingresa el precio del producto 

Opción del usuario: 4000

Ingresa la cantidad del producto

Opción del usuario: 10

El producto pan fue añadido exitosamente


**Opción 2**

Opción del usuario: 2 (Consultar producto)

Ingresa el nombre del producto: 

Opción del usuario: Fideos

El producto no existe en el inventario. Si desea crearlo ingrese a agregar producto.

**Opción 3**

Opción del usuario: 3 (Actualizar precio)

Ingresa el nombre del producto: 

Opción del usuario: leche de almendras

Ingrese un nuevo precio: 

Opción del usuario: 9000

Su producto: leche de almendras fue actualizado con éxito. Su nuevo precio es: 9000.

**Opción 4**

Opción del usuario: 4 (Eliminar producto)

Ingresa el nombre del producto: 

Opción del usuario: avena

El producto si se encuentra en el inventario con 60 existencias.

¿Estás seguro que deseas eliminarlo? [s/n]

Opción del usuario: s

Producto eliminado exitosamente

**Opción 5**

Opción del usuario: 4 (Calcular el valor total del inventario)

El total del inventario actual es: 406000.00


*Link repositorio:* https://github.com/angelicacvo/Prueba_gestion_estudiantes
