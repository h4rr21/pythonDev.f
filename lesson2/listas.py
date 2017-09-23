#Encoding
#-*- coding: utf-8 -*-


def saludar(nombre, mensaje="hola"):
    print mensaje, nombre


#saludar("h4rry")
#saludar("h4rry", "yellowñ")
#saludar(nombre="h4rry", mensaje="cómo vas?")


def play(intento=1):
    respuesta = raw_input("¿de qué color es un tomate?")
    if respuesta != "tomate":
        if intento < 3:
            print "\n Fallaste! Inténtalo de nuevo"
            intento += 1
            play(intento)
        else:
            print "\t\t Perdiste !"
    else:
        print "\t\t ganaste wey!!"

#play()

def printing():
    a,b,c = "string", 1556, False
    mi_tupla = ("yellow", False)
    texto, tu = mi_tupla
    print str(a)
    print str(b)
    print str(c)
    print str(texto), "-----> texto"
    print str(tu), "-----> tu"


#printing()


def the_while():
    while True:
        nombre = raw_input("Indique su nombre:\t")
        if nombre:
            print nombre
            break


#the_while()


def the_for():
    mi_lista = [67, 45, 2, "juan", True, False]
    for each_lista in mi_lista:
        print str(each_lista)
    mi_tupla = ("rosa", "verde", "rosa")
    for color in mi_tupla:
        print str(color)
    for anho in range(2013,2039,3):
        print "infor de cada anho",str(anho)

#the_for()
# productos
#2.5    1.4     4   1.2


lista = [6, 0]
productos = [2.5, 1.4, 1.2]
nombreNormal = 5


def imprimirProductos():
    print "Big Mac    --->  2.5 BTC"
    print "Big Whoop  --->  1.4 BTC"
    print "Bug Tank   --->  1.2 BTC"


def pedirDatos():
    global nombreNormal
    while lista[0] > 5:
        lista[0] = input("dame tus BTC!!\n")
    while nombreNormal!= 0:
        if lista[1] in productos:
            nombreNormal = 1
            break
        lista[1] = input("que producto quieres?" )

    return lista


def calcularVuelto(monto, precioProducto):
    if monto >= precioProducto:
        print "Tu cambio es:\t",monto - precioProducto
    else:
        print "no te alcanza el dinero"


def iniciar():
    lista1 = pedirDatos()
    calcularVuelto(lista1[0], lista1[1])


#imprimirProductos()
#iniciar()


#for i in range(1,10):
#    print "table del ", str(i)
#    for y in range(1,10):
#        print str(i), " * ", str(y), " = ", str(i*y)

for i in range(1, 10):
    print str(map(lambda x: x * i, range(1, 10)))