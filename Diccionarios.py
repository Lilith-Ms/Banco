# Creación
usuario = {"nombre": "Jazz", "edad": 21, "ciudad": "Acacías"}

# Acceder a un valor
r= usuario["edad"]  # Salida: Jazz

# Modificar un valor
usuario["edad"] = 28



# Añadir un nuevo par
usuario["profesion"] = "Ingeniero"



# Eliminar un elemento
del usuario["ciudad"]

# Usar el método get() para evitar errores si la clave no existe
email = usuario.get("email", "No proporcionado")
print(usuario.get("email", "No proporcionado"))

#Ejemplo de recorrido
for c, v in usuario.items():
    print (f"{c}xxxx:{v}")



personas = [{"nombre": "Jazz", "edad": 21, "ciudad": "Acacías"}
, {"nombre": "Ricardo", "edad": 27, "ciudad": "San Martín"}
, {"nombre": "Valeria", "edad": 20, "ciudad": "Granada"}
, {"nombre": "Luis", "edad": 33, "ciudad": "San Jose"}
, {"nombre": "Amanda", "edad": 18, "ciudad": "Guamal"}
, {"nombre": "Mónica", "edad": 29, "ciudad": "Acacías"}]

for j in personas:
    print (j)


print (personas[5]["edad"])


