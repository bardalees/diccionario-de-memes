word = input ("escribe una palabra que no entiendas (con mayusculas): ")
meme_dict = {
    "LOL" : "una respuesta a algo gracioso",
    "CRINGE" : "algo raro o embarazoso",
    "ROFL" : "una respuesta a una broma",
    "SHEESH" : "ligera desaprobación",
    "CREEPY" : "aterrador, siniestro",
    "AGGRO" : "ponerse agresivo/enojado",
}
if word in meme_dict.keys():
    print(f"{word}: {meme_dict[word]}")
else:
    print("La palabra no esta disponible en el diccionario")
