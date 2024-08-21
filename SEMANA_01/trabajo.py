
usuarios = [
    {"nombre": "Juan", "edad": 30},
    {"nombre": "Diana", "edad": 25},
    {"nombre": "Mario", "edad": 35}
]
resultado = [usuario for usuario in usuarios if usuario["edad"] > 30]

for usuario in resultado:
    print(usuario)
