'''
Los context managers son objetos de Python que proveen información contextual adicional al bloque de código. 
Esta información consiste en correr una función (o cualquier callable) cuando se inicia el contexto con el 
keyword with; al igual que correr otra función cuando el código dentro del bloque with concluye. Por ejemplo:

Existen dos formas de implementar un context manager: 
con una clase o con un generador. Vamos a implementar la funcionalidad anterior para ilustrar el punto:'''

#class
class CustomOpen(object):
    def __init__(self, filename):
        self.file = open(filename)

    def __enter__(self):
        return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.file.close()

with CustomOpen('file') as f:
    contents = f.read()


#generator
from contextlib import contextmanager

@contextmanager
def custom_open(filename):
    f = open(filename)
    try:
        yield f
    finally:
        f.close()

with custom_open('file') as f:
    contents = f.read()