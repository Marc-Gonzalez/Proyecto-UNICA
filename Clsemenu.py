class menuprincipal():
    def mensaje_bienvenida():

        print('****BIENVENIDO A EXPENDEDORA FI****\n')
    def mensaje_despedida():
        print('\n****GRACIAS VUELVA PRONTO****')

    mensaje_bienvenida()
    respuesta=None
    
    while respuesta != 0 :
        try:
            respuesta=int(input('Favor de ingresar una Opción (Solo Números):\n1.Mostrar y Escoger Golosinas\n2.2.Quitar golosinas\n3.Pagar\5.Salir\n'))
            #respuesta = respuesta  
    
            if respuesta == 1 :
                print('Porfavor elige tus golosinas\n')
                
                continue
            elif respuesta==2:
                print('aquie metemos una función que quite las golosinas\n')
                continue
            elif respuesta==3:
                print('Tu total a pagar es: \n') #Aquí hay que meter código para cobrar
                continue
            elif respuesta ==4:
                print('Salir\n')  
                break
                 
            else:
                print('Solo Ingresa números del 1 (uno) al 5 (cinco)\n')
                mensaje_despedida()
                
            
        except: 
            print('Opcion Invalida! SOLO PONER NUMEROS (SOLO NÚMEROS!!!!)')

        

menuprincipal()