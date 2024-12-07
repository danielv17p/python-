diccionario = {
    "estoico":"significa ser fuerte, ecuánime y sereno ante la desgracia",
    "Hedonista":"alguien que busca lo mejor ",
    "indulgente":"Inclinado a perdonar y disimular los yerros o a conceder gracias."
}

palabra = input("ingrese una palabra que no entienda?")

if palabra in diccionario.keys():
    print(diccionario[palabra])  
else : 
    print("no se encuentra esta palabra en este momento")
