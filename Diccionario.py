#creacion de diccionario
informacion_personal = {"nombre": "Ragna", "edad": "21", "ciudad": "Chone"}

#acceso y modificacion de valores
informacion_personal["profesion"] = "baterista"
informacion_personal["ciudad"] = "Quito"

#verificacion de existencia de clave
if "telefono" in informacion_personal:
    print("La clave existe")
else:
    print("La clave no existe")

#agregar clave "telefono"
informacion_personal["telefono"] = "0932554863"

#eliminacion de clave
del(informacion_personal["ciudad"])

#imprimir diccionario resultante
print(informacion_personal)


