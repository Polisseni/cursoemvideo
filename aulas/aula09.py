frase = ' Curso em Vídeo Python '
print(frase[:14])
print(frase[1:14:2])
print(frase[1::2])
print(frase[::2])
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip())) #remove espaços indesejados
print(frase.replace('Python','Android'))
print(frase.find('video')) #-1 significa False
print(frase.lower().find('vídeo'))
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])



#print("""Nature is a wondrous tapestry of life,
#filled with vibrant colors and sounds. From the
#gentle rustle of leaves in the wind to the melodious
#songs of birds at dawn, every element plays a
#role in this beautiful symphony. Mountains stand
#tall, reminding us of strength and stability, while
#rivers flow gracefully, symbolizing the journey of life.
#As seasons change, nature paints the world with different
#hues, inviting us to appreciate its beauty.
#Whether it's a serene forest or a bustling beach,
#spending time in nature rejuvenates the spirit and connects us to the Earth.""")
#Utilizar aspas 3x (""") no inicio e no final dos textos