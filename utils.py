def sumaDatos(datos):
    #Inicializamos la suma a 0
    suma = 0
    #Recorremos todos los datos recibidos
    for dato in datos:
        #Comprobamos si el datos se puede pasar a un numero real
        try:
            #Realizamos la suma
            suma = suma + float(dato)
        except ValueError:
            #En caso de que no se pueda pasar a float, no sera un numero y no realizamos nada 
            pass  
    #Devolvemos el valor de la suma de valores
    return suma