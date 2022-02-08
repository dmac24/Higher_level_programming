#!/usr/bin/python3
"""
Crea un archivo llamado models/base.py:

base de la clase:
atributo de clase privada __nb_objects = 0
constructor de clase: def __init__(self, id=Ninguno)::
si el id no es Ninguno, 
asigne el id del atributo de la instancia pública con este valor de argumento; 
puede suponer que el id es un número entero y no necesita probar su tipo
de lo contrario, incremente __nb_objects y asigne el nuevo valor a la identificación del atributo de la instancia pública
Esta clase será la "base" de todas las demás clases en este proyecto. 

"""
"""El objetivo es administrar el atributo de identificación en todas sus clases futuras y evitar duplicar el mismo código (por extensión, los mismos errores)"""

__nb_objects = 0

def __init__(self, id=None):
