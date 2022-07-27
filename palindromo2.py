palabra=input("ingrese palabra: ")

while palabra!="exit": 
    palabra_reversa=palabra[::-1]

    if palabra==palabra_reversa:
        print(palabra, "es una palabra palindroma")

    else:
        print(palabra, "no es una palabra palindroma")
    palabra=input("ingrese palabra: ")

