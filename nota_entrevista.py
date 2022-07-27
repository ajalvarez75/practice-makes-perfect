1 '''mutabilidad e inmutabilidad en python:

There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
*Set items are unchangeable, but you can remove and/or add items whenever you like.

'''

2 '''comprehensions, son una manera de crear listas en una sola linea, 
dicho de otra forma de forma simplificada pero elegante.

squares = [i**2 for i in range(1, 101) if i % 3 != 0]

my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
'''

3 '''coleccions, queues, order dicts:

En Python existen tres colecciones básicas, a saber: las listas, las tuplas y los diccionarios.''' 

4 '''GIL - global interpreter lock

The mechanism used by the CPython interpreter to assure that only 
one thread executes Python bytecode at a time.'''

5 '''concurrencia y paralelismo

- La concurrencia es la capacidad del CPU para procesar más de un proceso al mismo tiempo.
En la concurrencia, los procesos en ejecución no tienen por qué estar relacionados, es decir, 
cualquiera puede iniciar y terminar en el momento que sea.

El paralelismo sigue la filosofía de “divide y vencerás”, ya que consiste en tomar un único problema, 
y mediante concurrencia llegar a una solución más rápido. El paralelismo lo que hace es tomar el problema 
inicial, dividir el problema en fracciones más pequeñas, y luego cada fracción es procesada de forma 
concurrente, aprovechando al máximo la capacidad del procesador para resolver el problema. 
La principal diferencia del paralelismo contra la concurrencia es que, en el paralelismo, todos los 
procesos concurrentes están íntimamente relacionados a resolver el mismo problema, de tal forma que el 
resultado de los demás procesos afecta al resultado final.
'''

6 '''patrones de diseño, soluciones comunes a problemas comunes en programacion.

Un patrón de diseño debe cumplir al menos con los siguientes objetivos:

Estandarizar el lenguaje entre programadores
Evitar perder tiempo en soluciones a problemas ya resueltos o conocidos
Crear código reusable (excelente ventaja)

Los patrones de diseño se clasifican en tres tipos diferentes dependiendo del tipo de problema que resuelven. 
Estos pueden ser:

Creacionales: 
Estructurales
De comportamiento

++ Patrones creacionales
Su objetivo es resolver los problemas de creación de instancia. Estos ayudan a delegar responsabilidad de 
creación de objetos en situaciones necesarias.

Sus pilares fundamentales son encapsular el conocimiento de las clases y Ocultar cómo se crean y se instancian. 
Se subdividen a su vez así:

Singleton
(Instancia única): nos garantiza la existencia de una única instancia para una clase.

++ Patrones estructurales
se ocupan de resolver problemas sobre la estructura de las clases, es decir, 
se enfocan en cómo las clases y objetos se componen para formar estructuras mayores.

Decorator (Decorador):
Agrega funcionalidades a una clase de forma dinámica.

++ Patrones de comportamiento
Nos ayuda a resolver problemas relacionados con el comportamiento de la aplicación. Ofrece soluciones 
respecto a la interacción y responsabilidad entre objetos y clases. Por ejemplo:

Memento:
Se utiliza para restaurar el estado de un objeto a un estado anterior.

'''

7 '''herencia multiple, method resolution order python.
Is a rule that python follows to determinate when you run a method which one should be runned.

we can use mro() to know what is the order in which the class is going to check

class a:
    mun=10

class b(a):
    pass

class c(a):
    num=1

class d(b,c):
    pass

print(d.mro())
'''

8 '''generador o generadores, cual es la ventaja?, como se hacen:

permite un flujo de datos en tiempo real y tener cada uno de los 
datos solo cuando necesite ser consumido. Adicionalmente, será muy importante para garantizar un trabajo 
óptimo y equilibrio entre el procesado de datos (procesador) y la memoria principal (la memoria RAM).

● Generators are iterators which can execute only
once.
● Generator uses “yield” keyword.
● Generators are mostly used in loops to generate an
iterator by returning all the values in the loop without
affecting the iteration of the loop.
● Every Generator is an iterator


def generadora():
    n=1
    yield n

    n+=1
    yield n

    n+=1
    yield n

for i in generadora:
    print(n)

'''

9 '''first class function o funciones de primera clase.

Cuando una funcion es tratada como un objeto de primera clase.

++objeto de primera clase: es informacion que puede almacenarse en estruturas de datos, pasarse como
argumentos o usuarse en estructuras de control.

++propiedades de las funciones de primera clase:
-las funciones son objectos.
-las funciones se pueden pasar como argumentos a otras funciones.
-las funciones pueden devolver otra funcion.
'''

10 '''decoradores y como se hacen:
es una funcion la cual toma como input una funcion y a su vez retorna otra funcion.
sirve para modificar el comportamientode una funcion ya existente.

def decoradorA(parameter):
    def decoradorB(*args, **kwargs):
        print("paso 1")

        parameter(*args, **kwargs)
        print("paso final")
    return decoradorB

@decoradorA
def add(n1,n2):
    print(n1+n2)
add(5,10)

'''

11 '''formas de hacer una lista.
# empty list
my_list = []

# list of integers
my_list = [1, 2, 3]

# list with mixed data types
my_list = [1, "Hello", 3.4]

# nested list
my_list = ["mouse", [8, 4, 6], ['a']]

# Nested indexing
print(n_list[0][1])

print(n_list[1][3])'''

12 '''variable Global

Variables that are created outside of a function (as in all of the examples above) are known as 
global variables.

Global variables can be used by everyone, both inside of functions and outside.

def variable():
    global z
    z=1
variable()
print(z)'''

13 #nota: cuidado! nunca colocar cosas mutables como argunmento por defecto.

14 #version control system, ejemplo GIT y #GITHUB

15 '''diferencia entre merge and rebase, saber de rebase es opcional.
git merge al ser aplicado, mantiene a salvo la historia de la rama secundaria, ya que crea un nuevo commit 
que une ambas ramas sin “eliminarlas”, creando un nuevo punto de continuación que tiene 2 historias por 
detrás.
git rebase al ser aplicado, NO mantiene a salvo la historia de la rama secundaria, sino que “re-escribe” 
la historia de la rama principal integrando los commits de la rama secundaria en la rama principal, no crea 
un commit de unión adicional, sino que cambia el puntero (HEAD) al último commit que ubica.

git merge debería usarse para subir cambios y nuevas features a la rama principal y git rebase debería ser 
usado cuando se trata de integrar ramas secundarias.
.
Para la rama principal debemos tratar de mantener todo el detalle posible de la historia de trabajo, sin 
embargo para las ramas secundarias que deben unirse entre ellas, no es tan necesario hacer un seguimiento 
tan minucioso.'''

16 '''diferencia entre el operador == y el operador is
The Equality operator (==) is a comparison operator in Python that compare values of both the operands 
and checks for value equality. Whereas the ‘is’ operator is the  identity operator that checks whether both 
the operands refer to the same object or not (present in the same memory location).'''

17 #diferencia entre *args y **kwargs en Python.*

18 '''metodologia de trabajo scrum - o alguna otra agile methodology, opcional saber.
La metodología Scrum es un proceso para llevar a cabo un conjunto de tareas de forma regular con el objetivo 
principal de trabajar en equipo.
1. Planificación: Product Backlog
El Product Backlog es la fase en la que se establecen las tareas prioritarias y donde se obtiene información 
breve y detallada sobre el proyecto que se va a desarrollar.
2. Ejecución: Sprint
se produce el desarrollo de un producto que es entregable potencialmente.
3. Control: Burn Down
es la fase en la que se mide el progreso de un determinado proyecto Scrum.'''

19 '''context manager
Los context managers son objetos de Python que proveen información contextual adicional al bloque de código. 
Esta información consiste en correr una función (o cualquier callable) cuando se inicia el contexto con el 
keyword with; al igual que correr otra función cuando el código dentro del bloque with concluye. Por ejemplo:

Existen dos formas de implementar un context manager: 
con una clase o con un generador. Vamos a implementar la funcionalidad anterior para ilustrar el punto:

class file:
    #
    def __init__(self,filename, method):
        self.file=open(filename, method)

    def __enter__(self):
        print("enter")
        return self.file

    def __exit__(self, type,value,traceback):
        print("exit")
        self.file.close()

with file('file.txt', 'w') as f:
    print("something")
    f.write("hello")'''

20 #cuenta platzi: christopher.guzmanreyes@gmail.com contraseña: HagaleMijo2022.

21 https://www.efset.org/cert/RKxSCw