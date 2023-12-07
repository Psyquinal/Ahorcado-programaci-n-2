def CifradoCesar(texto, des):
    palabra = ""
    for caracter in texto:
        if caracter.isalpha():
            codigo = ord(caracter)
            if caracter.isupper():
                palabra += chr((codigo - 65 + des) % 26 + 65)
            else:
                palabra += chr((codigo - 97 + des) % 26 + 97)
        else:
            palabra += caracter
    return palabra

palabra = input("Ingrese la palabra a cifrar: ")

des = 2
PalabraCifrada = CifradoCesar(palabra, des)

print("Palabra cifrada:", PalabraCifrada)


