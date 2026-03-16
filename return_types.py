def obtener_precio_usuario(): 
    pregunta = input("Enter the item's price:\n")
    precioo= float(pregunta)
    return precioo
precio= obtener_precio_usuario()
print(precio)