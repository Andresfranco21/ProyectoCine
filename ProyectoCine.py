def datosCine(tipoPelicula,nombredePelicula,valorTicket,tipoSala):   
    cine = []
    cine.append(tipoPelicula)
    cine.append(nombredePelicula)
    cine.append(valorTicket)
    cine.append(tipoSala)
    return cine

def datosCombos(descripcionCombo,nombreCombo,precioCombo):
    combos = []
    combos.append(descripcionCombo)
    combos.append(nombreCombo)
    combos.append(precioCombo)
    return combos
    
def seleccionarPelicula(cine,nombrePelicula):
    for i in range(0, len(cine)):
        if nombrePelicula == cine[i][1]:
            return str(cine[i])

def seleccionarCombos(combos,nombreCombo):
    for i in range(0, len(combos)):
        if nombreCombo == combos[i][0]:
            return str(combos[i])

def sumatotal(precioCombo,valorTicket):
    cine = []
    combo = []
    
    total = precioCombo + valorTicket
    print(total)
    return total

def superAdiministrador():
        combos = []
        cine = []
        informacion = 1
        # continuar = True
        while informacion !=0:
            informacion = int(input("Ingrese: \n1 Para cargar informacion cine  \n2 Para Ingregar Combos\n3 Modulo de vendedor\n"))

            if informacion == 1:
                while informacion ==1:
                    tipoPelicula = input("Ingresa el genero de la pelicula \n")
                    nombredePelicula = input("Ingrese El nombre de la pelicula\n")
                    tipoSala = input("Ingrese tipo de sala \n")
                    valorTicket = int(input("ingrese valor ticket \n"))    
                    cine.append(datosCine(tipoPelicula,nombredePelicula,valorTicket,tipoSala))
                    informacion = int(input("1-Si desea volver al agregar peliculas\n2-Si desea agregar combo\n3-Si desea entrar al modulo de vendedor"))

            elif informacion == 2:
                while informacion == 2:
                    nombreCombo = str(input("Ingrese Nombre de combo, comida:\n"))
                    descripcionCombo = input("Ingrese Descripcion combo:\n")
                    precioCombo = float(input("Ingrese precio combo:\n"))
                    combos.append(datosCombos(nombreCombo,descripcionCombo,precioCombo))
                    informacion = int(input("3-Si desea ingresar al modulo de vededor\n"))

            elif informacion == 3:
                while informacion == 3:
                    print(cine)
                    print(combos)
                    nombredePelicula = (input("Ingresa el nombre de la pelicula\n"))
                    print(seleccionarPelicula(cine,nombredePelicula))
                    informacion = input("Desea Adicionar combo Si No")
        
            if informacion == "Si":
                while informacion == "Si":
                    print(combos)
                    nombreCombo = str(input("Ingrse el nombre del combo\n"))
                    print(seleccionarCombos(combos,nombreCombo))

                    informacion = int(input("Ingrese 9 para imprimir el tiquetet"))

            if informacion == 9:
                print("Usted selecciono la pelicula "+nombredePelicula+" Con el siguente Combo" + nombreCombo +"Gracias por su compra")
                print(sumatotal(valorTicket,precioCombo))
                
superAdiministrador()
