# Sistema de Gestión de Inventario - MENU 🌿

Un script interactivo desarrollado en **Python** para la administración de productos en un inventario mediante la consola (CLI). Este proyecto simula las operaciones básicas de un sistema de ventas para una tienda de jardinería, aplicando estructuras de datos dinámicas y validaciones robustas para garantizar la integridad de la información.

## 🚀 Características y Funcionalidades

El sistema implementa un menú interactivo en un bucle continuo (`while True`) que permite realizar las siguientes acciones:

1. **Ingresar un producto a vender:** Registro de nuevos artículos solicitando Nombre, Categoría y Precio.
2. **Visualizar productos:** Muestra de forma ordenada todos los elementos registrados en el sistema junto con el conteo total actual.
3. **Buscar un producto:** Búsqueda inteligente por nombre (insensible a mayúsculas y minúsculas).
4. **Eliminar un producto:** Remoción definitiva de un artículo del inventario seleccionándolo de forma simplificada a través de su número de índice.
5. **Finalizar:** Cierre controlado del programa de manera limpia.

## 🛠️ Robustez y Validaciones Incluidas

Para evitar fallos en tiempo de ejecución (*runtime errors*), el código cuenta con mecanismos de defensa clave:
* **Control de campos nulos:** El sistema no permite avanzar si el usuario ingresa datos vacíos.
* **Tipado estricto:** Conversión segura de tipos de datos (de cadenas `str` a enteros `int` para los precios).
* **Reglas de negocio:** Validación de precios para que no se admitan valores menores o iguales a cero.
* **Escudo de desbordamiento (IndexError):** Validación matemática de los índices seleccionados antes de aplicar operaciones de extracción en memoria (`.pop()`).

## 💻 Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Estructuras de datos:** Listas bidimensionales dinámicas (Listas de listas).
* **Métodos nativos utilizados:** `.append()`, `.pop()`, `.strip()`, `.capitalize()`, `.lower()`, `len()`.