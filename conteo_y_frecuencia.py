'Ejercicio: contar y buscar las palabras repetidas en el texto.'

text = "Creo que a veces es la gente de la que nadie espera nada, la que hace cosas que nadie puede imaginar. creo"

alvaro1 = text.lower()
'''lower no aplica a listas pero si texto'''

javier = alvaro1.replace(',','').replace('.','')
'''replace no aplica para listas pero si para texto'''

alvaro = javier.split(' ')
'''cuando se imprime arroja como resultado una lista de las palabras contenidas en text'''

diccionario = {}
for word in alvaro:
    if word in diccionario:
        diccionario[word] +=1

    else:
        diccionario[word] =1

for word in diccionario:
    frecuencia=diccionario[word]
    print(f"'{word}'{frecuencia}")
