import random
#import juego
vidas=5
vidas2=5
vidas3=5
villano=100
villano2=100
villano3=100
def p1():
	p = input("La subida al Monte Fuji solo está abierta al público desde el 1 de julio hasta el 27 de agosto de cada año. Alrededor de unas 200.000 personas suben al Monte Fuji durante este periodo de tiempo.\nComo media, ¿alrededor de cuántas personas suben al Monte Fuji cada día?\na)340 b)710 c)3400 d)7100\nRespuesta: ")
	if p=="c":
		global villano
		villano=villano-20
		print("¡Correcto!")
	else:
		global vidas
		vidas=vidas-1
		print("Incorrecto :(")
	global vagon1
	if villano<=0 and p1 in vagon1:
		vagon1.remove(p1)
	print("Vidas: {}".format(vidas))
	print("Vida del enemigo: {}".format(villano))
	print("\n")
	if p1 in vagon1:
		vagon1.remove(p1)
def p2():
	p=input("En un concierto de rock se reservó para el público un terreno rectangular con unas dimensiones de 100 m por 50 m. Se vendieron todas las entradas y el terreno se llenó de fans, todos de pie.\n¿Cuál de las siguientes cifras constituye la mejor estimación del número total de asistentes al concierto? Toma en cuenta que cada persona ocupa un m^2\na)2000 b)5000 c)20000 d)50000 e)100000\nRespuesta: ")
	if p=="b":
		global villano
		villano=villano-20
		print("¡Correcto!")
	else:
		global vidas
		vidas=vidas-1
		print("Incorrecto :(")
	global vagon1
	if villano<=0 and p2 in vagon1:
		vagon1.remove(p2)
	print("Vidas: {}".format(vidas))
	print("Vida del enemigo: {}".format(villano))
	print("\n")
	if p2 in vagon1:
		vagon1.remove(p2)
def p3():
	p = input("¿Para qué sirve el triángulo de Pascal?\na)Para Derivar funciones trigonométricas b)Para calcular binomios a la n potencia c)Para integrar funciones trigonométricas d)Para multiplicar matrices\n")
	if p=="b":
		global villano
		villano=villano-20
		print("¡Correcto!")
	else:
		global vidas
		vidas=vidas-1
		print("Incorrecto :(")
	global vagon1
	if villano<=0 and p3 in vagon1:
		vagon1.remove(p3)
	print("Vidas: {}".format(vidas))
	print("Vida del enemigo: {}".format(villano))
	print("\n")
	if p3 in vagon1:
		vagon1.remove(p3)
def p4():
	p = input("¿Qué determina el pH de una sustancia?\na) Si es ácida o básica b)Su solubilidad en agua c)Su viscosidad d)Su masa molar\nRespuesta: ")
	if p=="a":
		global villano
		villano=villano-20
		print("¡Correcto!")
	else:
		global vidas
		vidas=vidas-1
		print("Incorrecto :(")
	global vagon1
	if villano<=0 and p4 in vagon1:
		vagon1.remove(p4)
	print("Vidas: {}".format(vidas))
	print("Vida del enemigo: {}".format(villano))
	print("\n")
	if p4 in vagon1:
		vagon1.remove(p4)
def p5():
	print("¿Quién fue el primer presidente de México?")
	p=input("a)Vicente Guerrero b)Guadalupe victoria c)Anastasio Bustamante\nRespuesta: ")
	if p=="b":
		global villano
		villano=villano-20
		print("¡Correcto!")
	else:
		global vidas
		vidas=vidas-1
		print("Incorrecto :(")
	global vagon1
	if villano<=0 and p5 in vagon1:
		vagon1.remove(p5)
	print("Vidas: {}".format(vidas))
	print("Vida del enemigo: {}".format(villano))
	print("\n")
	if p5 in vagon1:
		vagon1.remove(p5)
def p6():
	print("¿En que año se disolvió la Unión Sovietica?")
	p=input(" a)1991  b)1987  c)1993: ")
	if p=="a":
		global villano
		villano=villano-20
		print("¡Correcto!")
	else:
		global vidas
		vidas=vidas-1
		print("Incorrecto :(")
	global vagon1
	if villano<=0 and p6 in vagon1:
		vagon1.remove(p6)
	print("Vidas: {}".format(vidas))
	print("Vida del enemigo: {}".format(villano))
	print("\n")
	if p6 in vagon1:
		vagon1.remove(p6)
def p7():
	print("¿Quién fue el primer emperador romano?")
	p=input(" a)Rómulo Augusto  b)César Augusto  c)Tibero Claudio: ")
	if p=="b":
		global villano
		villano=villano-20
		print("¡Correcto!")
	else:
		global vidas
		vidas=vidas-1
		print("Incorrecto :(")
	global vagon1
	if villano<=0 and p7 in vagon1:
		vagon1.remove(p7)
	print("Vidas: {}".format(vidas))
	print("Vida del enemigo: {}".format(villano))
	print("\n")
	if p7 in vagon1:
		vagon1.remove(p7)
def p8():
	print("¿En que país nación Adolf Hitler?")
	p=input(" a)Alemania  b)Polonia  c)Austria: ")
	if p=="c":
		global villano
		villano=villano-20
		print("¡Correcto!")
	else:
		global vidas
		vidas=vidas-1
		print("Incorrecto :(")
	global vagon1
	if villano<=0 and p8 in vagon1:
		vagon1.remove(p8)
	print("Vidas: {}".format(vidas))
	print("Vida del enemigo: {}".format(villano))
	print("\n")
	if p8 in vagon1:
		vagon1.remove(p8)
def p9():
	print("¿Quién inventó la bombilla elétrica?")
	p=input("a)Thomas Edison  b)Nikola Tesla  c)Alexander Bell: ")
	if p=="a":
		global villano2
		villano2=villano2-20
		print("¡Correcto!")
	else:
		global vidas2
		vidas2=vidas2-1
		print("Incorrecto :(")
	global vagon2
	if villano2<=0 and p9 in vagon2:
		vagon2.remove(p9)
	print("Vidas: {}".format(vidas2))
	print("Vida del enemigo: {}".format(villano2))
	print("\n")
	if p9 in vagon2:
		vagon2.remove(p9)
def p10 ():
	p=input("¿Quién inventó la bombilla eléctrica?\n a) Thomas Edison  b)Nikola Tesla  c)Alexander Bell: ")
	if p=="a":
		global villano2
		villano2=villano2-20
		print("¡Correcto!")
	else:
		global vidas2
		vidas2=vidas2-1
		print("Incorrecto :(")
	global vagon2
	if villano2<=0 and p10 in vagon2:
		vagon2.remove(p10)
	print("Vidas: {}".format(vidas2))
	print("Vida del enemigo: {}".format(villano2))
	print("\n")
	if p10 in vagon2:
		vagon2.remove(p10)
def p11 ():
	p=input("¿Por qué la iglesia condenó a Galileo Galilei?\n a)Por ser judío  b)Por decir que la tierra giraba alrededor del Sol  c)Por atentar contra un sacerdote\n Respuesta: ")
	if p=="b":
		global villano2
		villano2=villano2-20
		print("¡Correcto!")
	else:
		global vidas2
		vidas2=vidas2-1
		print("Incorrecto :(")
	global vagon2
	if villano2<=0 and p11 in vagon2:
		vagon2.remove(p11)
	print("Vidas: {}".format(vidas2))
	print("Vida del enemigo: {}".format(villano2))
	print("\n")
	if p11 in vagon2:
		vagon2.remove(p11)
def p12 ():
	p=input("¿Cómo se llamaba el primer presidente de Estados Unidos?\n a)Abraham Lincoln  b)Thomas Jefferson  c)George Washington\n Respuesta: ")
	if p=="c":
		global villano2
		villano2=villano2-20
		print("¡Correcto!")
	else:
		global vidas2
		vidas2=vidas2-1
		print("Incorrecto :(")
	global vagon2
	if villano2<=0 and p12 in vagon2:
		vagon2.remove(p12)
	print("Vidas: {}".format(vidas2))
	print("Vida del enemigo: {}".format(villano2))
	print("\n")
	if p12 in vagon2:
		vagon2.remove(p12)
def p13 ():
	print("¿En que año comenzó la guerra fría?")
	p=input(" a)1947  b)1948  c)1949\nRespuesta: ")
	if p=="a":
		global villano2
		villano2=villano2-20
		print("¡Correcto!")
	else:
		global vidas2
		vidas2=vidas2-1
		print("Incorrecto :(")
	global vagon2
	if villano2<=0 and p13 in vagon2:
		vagon2.remove(p13)
	print("Vidas: {}".format(vidas2))
	print("Vida del enemigo: {}".format(villano2))
	print("\n")
	if p13 in vagon2:
		vagon2.remove(p13)
def p14 ():
	p=input(" ¿En qué año se fundó la ONU?\n a)1939 b)1949 c)1945\n Respuesta: ")
	if p=="c":
		global villano2
		villano2=villano2-20
		print("¡Correcto!")
	else:
		global vidas2
		vidas2=vidas2-1
		print("Incorrecto :(")
	global vagon2
	if villano2<=0 and p14 in vagon2:
		vagon2.remove(p14)
	print("Vidas: {}".format(vidas2))
	print("Vida del enemigo: {}".format(villano2))
	print("\n")
	if p14 in vagon2:
		vagon2.remove(p14)
def p15 ():
	p=input(" ¿Quién inventó la dinamita?\n a)Albert Einstein b)Alfred Nobel c)Alfred Hitchcock\n Respuesta: ")
	if p=="b":
		global villano2
		villano2=villano2-20
		print("¡Correcto!")
	else:
		global vidas2
		vidas2=vidas2-1
		print("Incorrecto :(")
	global vagon2
	if villano2<=0 and p15 in vagon2:
		vagon2.remove(p15)
	print("Vidas: {}".format(vidas2))
	print("Vida del enemigo: {}".format(villano2))
	print("\n")
	if p15 in vagon2:
		vagon2.remove(p15)
def p17():
	p= input("¿Qué determina el pH de una sustancia? \n  a)Si es ácida o básica b)Su solubilidad en agua c)Su viscosidad d)Su masa molar\nRespuesta: ")
	if p=="a":
		global villano3
		villano3=villano3-20
		print("¡Correcto!")
	else:
		global vidas3
		vidas3=vidas3-1
		print("Incorrecto :(")
	print("Vidas: {}".format(vidas3))
	print("Vida del enemigo: {}".format(villano3))
	print("\n")
	global vagon3
	vagon3.remove(p17)
def p18():
	p= input("¿Qué funciones trigonométricas son recíprocas? \n a)Seno y coseno, tangente y cotangente, secante y cosecante b)Seno y secante, coseno y cosecante, tangente y cotangente c)Seno y cosecante, coseno y secante, tangente y cotangente d)Seno y tangente, coseno y cotangente, tangente y secante\nRespuesta: ")
	if p=="c":
		global villano3
		villano3=villano3-20
		print("¡Correcto!")
	else:
		global vidas3
		vidas3=vidas3-1
		print("Incorrecto :(")
	print("Vidas: {}".format(vidas3))
	print("Vida del enemigo: {}".format(villano3))
	print("\n")
	global vagon3
	vagon3.remove(p18)
def p19():
	p= input("¿Cuál de los siguientes elementos es más electronegativo? \n a)Oxígeno b)Neón c)Aluminio d)Berilio\nRespuesta: ")
	if p=="a":
		global villano3
		villano3=villano3-20
		print("¡Correcto!")
	else:
		global vidas3
		vidas3=vidas3-1
		print("Incorrecto :(")
	print("Vidas: {}".format(vidas3))
	print("Vida del enemigo: {}".format(villano3))  
	print("\n")
	global vagon3
	vagon3.remove(p19)
def p20():
	p= input("¿Cuál de éstas no es una etapa del ciclo hidrológico? \n a)Condensación b)Evaporación c)Perforación d)Escurrimiento\nRespuesta: ")
	if p=="c":
		global villano3
		villano3=villano3-20
		print("¡Correcto!")
	else:
		global vidas3
		vidas3=vidas3-1
		print("Incorrecto :(")
	print("Vidas: {}".format(vidas3))
	print("Vida del enemigo: {}".format(villano3))
	print("\n")
	global vagon3
	vagon3.remove(p20)
def p21():
	p= input("¿Cómo se calcula la potencia?\n a)Fuerza*distancia b)Fuerza/área c)Fuerza/aceleración d)Masa/aceleración\nRespuesta: ")
	if p=="a":
		global villano3
		villano3=villano3-20
		print("¡Correcto!")
	else:
		global vidas3
		vidas3=vidas3-1
		print("Incorrecto :(")
	print("Vidas: {}".format(vidas3))
	print("Vida del enemigo: {}".format(villano3))
	print("\n")
	global vagon3
	vagon3.remove(p21)
def p22():
	p= input("¿Qué partícula subatómica no posee carga eléctrica? \n a)Electrón b)Neutrón c)Protón d)Fotón\nRespuesta: ")
	if p=="b":
		global villano3
		villano3=villano3-20
		print("¡Correcto!")
	else:
		global vidas3
		vidas3=vidas3-1
		print("Incorrecto :(")
	print("Vidas: {}".format(vidas3))
	print("Vida del enemigo: {}".format(villano3))
	print("\n")
	global vagon3
	vagon3.remove(p22)
def p23():
	p= input("¿Para qué tipo de triángulo es aplicable el Teorema de Pitágoras? \n a)Isósceles b)Equilátero c)Rectángulo d)Oblicuángulo\nRespuesta: ")
	if p=="c":
		global villano3
		villano3=villano3-20
		print("¡Correcto!")
	else:
		global vidas3
		vidas3=vidas3-1
		print("Incorrecto :(")
	print("Vidas: {}".format(vidas3))
	print("Vida del enemigo: {}".format(villano3))
	print("\n")
	global vagon3
	vagon3.remove(p23)
def p24():
	p= input("¿Cuál de lo siguientes no es un tipo de reacción química? \n a)Sustitución simple b)Fijación c)Síntesis d)Descomposición\nRespuesta: ")
	if p=="b":
		global villano3
		villano3=villano3-20
		print("¡Correcto!")
	else:
		global vidas3
		vidas3=vidas3-1
		print("Incorrecto :(")
	print("Vidas: {}".format(vidas3))
	print("Vida del enemigo: {}".format(villano3))
	print("\n")
	global vagon3
	vagon3.remove(p24)
def pcontrol1():
	p= input("¿Quieres seguir jugando?\n (Y/N)\n")
	if p=="y":
		print("\n")
	else:
		exit()
def pcontrol2():
	p= input("¿Quieres seguir jugando?\n (Y/N)\n")
	if p=="y":
		print("\n")
	else:
		exit()
def pcontrol3():
	p= input("¿Quieres seguir jugando?\n (Y/N)\n")
	if p=="y":
		print("\n")
	else:
		exit()
vagon1=[p1,p2,p3,p4,p5,p6,p7,p8,pcontrol1]
vagon2=[p9,p10,p11,p12,p13,p14,p15,pcontrol2]
vagon3=[p17,p18,p20,p21,p22,p23,p24,pcontrol3]
def play():
	while True:
		nivel1 = random.choice(vagon1)
		nivel2 = random.choice(vagon2)
		nivel3 = random.choice(vagon3)
		nivel1()
		if vidas <=0:
			print("Perdiste tus vidas, estás muerto.")
			exit()
		elif villano <=0:
			if p1 in vagon1:
				vagon1.remove(p1)
			if p2 in vagon1:
				vagon1.remove(p2)
			if p3 in vagon1:
				vagon1.remove(p3)
			if p4 in vagon1:
				vagon1.remove(p4)
			if p5 in vagon1:
				vagon1.remove(p5)
			if p6 in vagon1:
				vagon1.remove(p6)
			if p7 in vagon1:
				vagon1.remove(p7)
			if p8 in vagon1:
				vagon1.remove(p8)
			if villano2==100:
				print("NIVEL 2\n")
			nivel2()
			if vidas2 <=0:
				print("Perdiste tus vidas, estás muerto.")
				exit()
			elif villano2 <=0:
				if p9 in vagon2:
					vagon2.remove(p9)
				if p10 in vagon2:
					vagon2.remove(p10)
				if p11 in vagon2:
					vagon2.remove(p11)
				if p12 in vagon2:
					vagon2.remove(p12)
				if p13 in vagon2:
					vagon2.remove(p13)
				if p14 in vagon2:
					vagon2.remove(p14)
				if p15 in vagon2:
					vagon2.remove(p15)
				if villano3==100:
					print("NIVEL 3\n")
				nivel3()
				if vidas3 <=0:
					print("Perdiste tus vidas, estás muerto.")
					exit()
				elif villano3 <=0:
					print("!Ganaste, eres un genio!")
					#exit()
#play()
#juego.grafica()