class golosinas():
    def dulces():
        listadedulces = int(input('escoger la categoria de dulces:1.paletas\n2.chocolates\n3.gomitas\n'))
        
        if listadedulces == 1:
                elementosdulces = ['manita','bubbalo','rockaleta']

                print('lista de paletas: \n',elementosdulces)

                op2 = int(input('ingrese la paleta'))
                
                if op2 == 1:
                        print(elementosdulces[0])
                elif op2 == 2:
                        print(elementosdulces[1])
                elif op2 == 3:
                        print(elementosdulces[2])
                else:
                        print('no existe opcion')
                
        elif listadedulces == 2:
                    elementosdulcesch = ['ferrero roche','carlos v','bubu lubu']
                    print('lista de paletas: \n',elementosdulcesch)
                    op2 = int(input('ingrese la paleta'))
                    if op2 == 1:
                        print(elementosdulcesch[0])
                    elif op2 == 2:
                        print(elementosdulcesch[1])
                    elif op2 == 3:
                        print(elementosdulcesch[2])
                    else:
                        print('no existe opcion')

        elif listadedulces == 3:
                    elementosdulcesgo = ['panditas','pinguinos','gomitas de azuzcar']
                    print('lista de gomitas: \n',elementosdulcesgo)
                    op2 = int(input('ingrese las gomitas'))
                    if op2 == 1:
                        print(elementosdulcesgo[0])
                    elif op2 == 2:
                        print(elementosdulcesgo[1])
                    elif op2 == 3:
                        print(elementosdulcesgo[2])
                    else:
                        print('no existe opcion')
        else:
            print('no hay opciones')
                         
                        
golosinas.dulces()
