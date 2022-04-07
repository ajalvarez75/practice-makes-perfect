'Ejercicio: contar y buscar las palabras repetidas en el texto.'

text = "Creo que a veces es la gente de la que nadie espera nada, la que hace cosas que nadie puede imaginar. creo"

eliminar = ",;:.\n!\"´'"

text = text.lower()
'''se convierte el texto a minisculas'''

for puntuaciones in eliminar:
    text=text.replace(puntuaciones,'')
'''se aplica variable eliminar al texto con el fin de reemplazar carateres'''

texto = text.split()    
'''se divide el texto a arreglo'''
    
diccionary = {}
'''se declara diccionario'''

for n in texto:
    '''se cuentan los elementos en el texto para ello se creo el diccionario
    la clave seran los elementos y el valor sera el conteo'''
    if n in diccionary:
        diccionary[n] +=1
    else:
        diccionary[n] =1

for n in diccionary:
    '''for para crear la frecuencia de los elementos en el diccionario'''
    frecuencia = diccionary[n]
    print(f"{n} = {frecuencia}")
    '''f funciona para darle el valor/formato correspondiente a n y frecuencia'''
    
