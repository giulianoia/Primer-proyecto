productos = []

print("\n\n\t---------- MENU ----------")

while True:
    # Interfaz
    print("\n SELECCIONAR UNA OPCION:\n")

    print("1-Ingresar un producto a vender")
    print("2-Visualizar los productos ingresados")
    print("3-Buscar un producto")
    print("4-Eliminar un producto")
    print("5-Finalizar\n")

    opcion = input("Ingrese su opcion: 1-5\n").strip()

    # ------------------------------------------------------------------------
    # Opción vacia
    # ------------------------------------------------------------------------

    if not opcion:
        print("Error, no se puede ingresar nulo")
        continue

    # ------------------------------------------------------------------------
    # Opción 1: AGREGAR PRODUCTO
    # ------------------------------------------------------------------------

    if opcion == "1":   #Ingresar un producto
        print("\nAGREGAR PRODUCTO A LA VENTA:")

        #Solicitamos los datos y verificamos que no esten vacios, ni erroneos.
        while True:
            nombre=input("Nombre del producto: ").strip().capitalize()
            if nombre=="":
                print("Por favor ingrese un nombre para el producto...")
                continue
            break
        
        while True:
            categoria=input("Ingrese la categoria del producto: ").strip().capitalize()
            if categoria=="":
                print("Pr favor ingrese una categoria...")
                continue
            break

       
        while True:
            precioc=input("Ingrese el precio del producto: ").strip()
            if precioc=="": #No puede estar vacio
                print("Por favor, no puede estar vacio...")
                continue
            precio=int(precioc) #pasamos el string precioc a int precio

            if precio <= 0:
                print("Por favor, el precio no puede ser menor a 0 o gratuito...")
                continue
            break
        nuevo_producto= [nombre, categoria, precio]
        productos.append(nuevo_producto)
        print(f"Producto '{nombre}'agregado con exito")
  
    # ------------------------------------------------------------------------
    # Opción 2: VISUALIZAR PRODUCTOS
    # ------------------------------------------------------------------------

    elif opcion== "2": 
        print("\n---------- LISTA DE PRODUCTOS REGISTRADOS ----------")
        if len(productos) == 0:
            print("No hay ningun producto...")
            continue
        else:
            print(f"Productos registrados: ({len(productos)})")
            for producto in productos:
                print(f"Producto: {producto[0]} / Categoria: {producto[1]} / precio: ${producto[2]}")
        print("-" * 50)
    
        
    # ------------------------------------------------------------------------
    # Opción 3: Buscar producto
    # ------------------------------------------------------------------------

    elif opcion == "3":
        print("\n---BUSCAR UN PRODUCTO---")
        if len(productos) == 0:
            print("No hay ningun producto...")
            continue

        busqueda=input("Ingrese el nombre del producto que desea buscar: \n").strip().lower()

        if busqueda=="":
            print("No se puede dejar nulo...")
            continue # Usamos continue para que vuelva a mostrar el menú o pedir el dato
        
        encontrado = False
        for producto in productos:
            if producto[0].lower() == busqueda:
                print(f"\nProducto encontrado: {producto[0]} / Categoria: {producto[1]} / Precio: ${producto[2]}")
                encontrado=True
                break # Este break es para salir del ciclo FOR, no del menú
        if encontrado == False:
            print("\nEl producto no se encuentra en el inventario.")


    # ------------------------------------------------------------------------
    # Opción 4: Eliminar Producto
    # ------------------------------------------------------------------------

    elif opcion == "4": #Eliminar un producto
        print("\n---ELIMINAR PRODUCTO---")
        if len(productos) == 0:
            print("No hay ningun producto...")
            continue

        # Mostramos los productos disponibles para eliminar:
        print("\n Productos disponibles para eliminar: \n")
    
        for i in range(len(productos)):
            print(f"{i+1}-{productos[i][0]} - ${productos[i][2]}")

        indice = input("Ingrese el numero del producto que quiere eliminar: ").strip()
        if indice == "":
            print("No puede ser nulo...") 
            continue   
        
        # Guardamos el número en 'idx'
        idx = int(indice) - 1

        # Controlamos que 'idx' sea válido
        if idx >= 0 and idx < len(productos):
            borrar = productos.pop(idx)
            print(f"\nProducto '{borrar[0]}' eliminado correctamente.")
        else:
            print("Indice no válido.")



    # ------------------------------------------------------------------------
    # Opción 5: Finalizar
    # ------------------------------------------------------------------------    
    #elif opcion == "5": #Salir del programa






    