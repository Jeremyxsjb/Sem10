print ("-----Bienvenido a calcula tu descuento diario-----")
print ("-----Por favor digite el precio-----")
print ("-----Aplicaremos el descuento del dia de hoy------")


pre = int(input("precio: "))
cant = int(input("cantidad: "))
sub = pre * cant
desc = sub * 0.25
tot = sub - desc
print("Subtotal: ", sub)
print("Descuento: ", desc)
print("Total a pagar: ", tot)
