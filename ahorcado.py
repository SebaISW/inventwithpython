import random
IMAGENES_AHORCADO = ['''
+---+
| |
|
|
|
|
=========''','''
+---+
|   |
O   |
    |
    |
    |
  =========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''
+---+
 |  |
 O  |
/|\ |
/ \ |
    |
=========''']
#palabras = "hormiga babuino tejon murcielago oso castor camello gato \
#almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro \
#rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra \
#nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte \
#salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre \
#sapo trucha pavo tortuga comadreja ballena lobo wombat cebra".split()
palabras = {'Colores' : 'rojo naranja amarillo verde azul violeta blanco negro marron'.split(),
'Formas' : 'cuadrado triangulo rectangulo circulo elipse rombo trapezoide pentagono hezagono heptagono octogono'.split(),
'Frutas' : 'manzana naranja limon lima pera sandia uva cereza banana melon mango fresa tomate'.split()
'Animales' : 'murcielago oso castor gato pantera cangrejo ciervo perro burro pato aguila pez rana\
cabra sanguijuela leon lagarto mono alce raton nutria buho panda conejo rata tiburon oveja tigre pavo toruga comadrejaballena lobo cebra'.split()}
def obtenerPalabra(diccionarioDePalabras):
#  indiceDePalabras=random.randint(0, len(listaDePalabras) -1)
#  return listaDePalabras[indiceDePalabras]
   claveDePalabra=random.choice(list(diccionarioDePalabras.keys()))
   indiceDePalabra=random.randint(len(diccionarioDePalabras[claveDePalabras][indiceDePalabra],[claveDePalabra]))
def mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas,palabraSecreta):
  print(IMAGENES_AHORCADO[len(letrasIncorrectas)])
  print()

  print('Letras Incorrectas: ', end=' ')
  for letra in letrasIncorrectas:
    print(letra, end= ' ')
  print()

  espaciosVacios= '_' * len(palabraSecreta)
  for i in range(len(palabraSecreta)):
    if palabraSecreta[i] in letrasCorrectas:
      espaciosVacios = espaciosVacios[:i] + palabraSecreta[i] + espaciosVacios[i+1:]
  for letra in espaciosVacios:
    print(letra, end=' ')
    print()
def obtenerIntento(letrasProbadas):
  while True:
    print('Adivina una letra.')
    intento=input()
    intento=intento.lower()
    if len(intento) != 1:
      print('Por faor introduce una letra.')
    elif intento in letrasProbadas:
      print('ya has probado esa letra. Elige otra')
    elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
      print('Por favor elige una LETRA')
    else:
      return intento
def jugarDeNuevo():
  print('Quieres Jugar de nuevo (si o no)')
  return input().lower().startswith('s')
print('A H O R C A D O')
letrasIncorrectas=''
letrasCorrectas=''
palabraSecreta=obtenerPalabra(palabras)
juegoTerminado= False
while True:
 mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
 print(palabraSecreta)
 intento = obtenerIntento(letrasCorrectas + letrasIncorrectas)
 if intento in palabraSecreta:
   letrasCorrectas = letrasCorrectas + intento
   encontradoTodasLasLetras = True
   for i in range(len(palabraSecreta)):
    if palabraSecreta[i] not in letrasCorrectas:
     encontradoTodasLasLetras = False
     break
   if encontradoTodasLasLetras:
      print('Si! la Palabra secreta es ', palabraSecreta, 'Has ganado')
      juegoTerminado = True
 else:
    letrasIncorrectas = letrasIncorrectas + intento
    if len(letrasIncorrectas) == len(IMAGENES_AHORCADO) - 1:
      mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
      print('Te has quedado sin intentos!\nDespues de ', str(len(letrasIncorrectas)),'intentos fallidos y ', str(len(letrasCorrectas)), ' aciertos, la palabra era "', palabraSecreta,'"')
      juegoTerminado = True
 if juegoTerminado:
  if jugarDeNuevo():
    letrasCorrectas = ''
    letrasIncorrectas = ''
    juegoTerminado = False
    palabraSecreta = obtenerPalabra(palabras)
  else:
    print('Gracias por Jugar!')
    break