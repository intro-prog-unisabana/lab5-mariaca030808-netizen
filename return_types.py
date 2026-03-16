def obtener_precio_usuario(): 
    pregunta = input("Enter the item's price:\n")
    precio= float(pregunta)
    return precio
precio= obtener_precio_usuario()
print(precio)