# solucion_diccionario_contactos.py
# Definición de un diccionario con información de contacto.
contactos = {
    "Juan": {"telefono": "123456789", "email": "juan@example.com"},
    "Ana": {"telefono": "987654321", "email": "ana@example.com"}
}

# Agregar un nuevo contacto al diccionario.
contactos["Maria"] = {"telefono": "555555555", "email": "maria@example.com"}
print(contactos)  # Output: {'Juan': {'telefono': '123456789', 'email': 'juan@example.com'}, 'Ana': {'telefono': '987654321', 'email': 'ana@example.com'}, 'Maria': {'telefono': '555555555', 'email': 'maria@example.com'}}

# Actualizar el número de teléfono de un contacto existente.
contactos["Juan"]["telefono"] = "111111111"
print(contactos)  # Output: {'Juan': {'telefono': '111111111', 'email': 'juan@example.com'}, 'Ana': {'telefono': '987654321', 'email': 'ana@example.com'}, 'Maria': {'telefono': '555555555', 'email': 'maria@example.com'}}

# Eliminar un contacto del diccionario.
del contactos["Ana"]
print(contactos)  # Output: {'Juan': {'telefono': '111111111', 'email': 'juan@example.com'}, 'Maria': {'telefono': '555555555', 'email': 'maria@example.com'}}
