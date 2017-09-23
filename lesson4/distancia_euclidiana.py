from math import sqrt, pow


def distanciaEuclidiana():
    distancia1 = 0
    P1 = raw_input("dame el punto 1:\t").split(",")
    P2 = raw_input("dame el punto 2:\t").split(",")

    if len(P1) == len(P2) and len (P1) >1:
        for i in range(len(P2)):
            distancia1 += pow((int(P2[i])-int(P1[i])), 2)
        return str(sqrt(distancia1))
    else:
        return "Input Error"


print distanciaEuclidiana()


#distancia = sqrt(pow((int(P2[0])-int(P1[0])),2) + pow((int(P2[1])-int(P1[1])),2))
        #print str(distancia)