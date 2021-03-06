# -*- coding: utf-8 -*-

def rotor(letra, numero, inverso=False): #letra: número asociado a esa letra, número: equivalene al rotor
    """
    letra: Número asociado a esa letra
    número: equivalente al rotor
    """
    I=[4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
    II=[0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
    III=[1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
    """ """
    IV=[4, 18, 14, 21, 15, 25, 9, 0, 24, 16, 20, 8, 17, 7, 23, 11, 13, 5, 19, 6, 10, 3, 2, 12, 22, 1]
    V=[21, 25, 1, 17, 6, 8, 19, 24, 20, 15, 18, 3, 13, 7, 11, 23, 0, 22, 12, 9, 16, 14, 5, 4, 2, 10]
    tipo=[I,II,III,IV,V]
    if inverso==False:
        x=tipo[numero-1][(letra)%26]
    else:
        x=tipo[numero-1].index((letra)%26)
    return x

def enigma(texto, numeros, posiciones, cambios=list(range(26))):
    """
    texto: Texto a cifrar (en mayúsculas, sin eñes ni espacios)
    numeros: Lista de los rotores a utiizar en el orden deseado
    posiciones: Vector con sus posiciones iniciales
    cambios: Lista de los cambios
    """
    girador=[16, 4, 21, 9, 25] 
    lista=list(texto)
    listacif=[] 
    letras=[ord(letra)-65 for letra in lista]
    for letra in letras:
        letra=cambios[letra]
        posiciones[2]=(posiciones[2]+1)%26
        if posiciones[2]==girador[numeros[2]-1]+1:
            posiciones[1]=(posiciones[1]+1)%26
        if posiciones[1]==girador[numeros[1]-1]:
            posiciones[0]=(posiciones[0]+1)%26
            posiciones[1]+=1
        rotor1=rotor((letra+posiciones[2])%26, numeros[2])
        rotor2=rotor((rotor1-(posiciones[2]-posiciones[1]))%26, numeros[1])
        rotor3=rotor(rotor2-(posiciones[1]-posiciones[0])%26, numeros[0])
        R=[24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]
        reflejado=R[rotor3-posiciones[0]]
        rotor3=rotor(reflejado+posiciones[0], numeros[0], True)
        rotor2=rotor(rotor3+(posiciones[1]-posiciones[0])%26, numeros[1], True)
        rotor1=(rotor(rotor2+(posiciones[2]-posiciones[1])%26, numeros[2], True)-posiciones[2])%26
        letra=cambios[rotor1]
        listacif.append(letra)
    listafin=[chr(letra+65) for letra in listacif]
    listafin=''.join(listafin)
    return listafin

print(enigma('EUREKA',[4,5,1],[5,4,17],[11, 1, 2, 20, 4, 5, 6, 7, 8, 9, 10, 0, 12, 13, 14, 15, 16, 17, 18, 19, 3, 21, 22, 23, 24, 25]))

print(enigma('UFKNRUBGNMFIYEBUQLBNPTTTAQYCBRNUPEDUIXUDSRJOVGWUYTEVLVURHQPKUPVNUWQOFOUIDUQZJTPQFMVIYSBLBZWFHWLSZWFWILUPWXUCGTIALYFBXUVJHFVMQGMXOCNMJZYYEPJNBSIBBTJUZQIEOGLFNVNIOCRWQTGJASOLVWNIEZJNYQNACHRZRTGHCDYFZWSZFCYATXFDGRCESZUNSQDLFJWCNOEZMNSFDUMOBSFOMYAQIINRGPIUEBRHOVLDFOKIVVGTOJYMDGVHVYSEDAAZQMOPZJFYNMCHRHIQI',[1,2,3],[15,23,13],[11, 1, 2, 20, 4, 5, 6, 7, 8, 9, 10, 0, 12, 13, 14, 15, 16, 17, 18, 19, 3, 21, 22, 23, 24, 25]))
