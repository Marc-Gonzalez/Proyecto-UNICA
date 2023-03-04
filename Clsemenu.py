class menuprincipal():
    def mensaje_bienvenida():

        print('****BIENVENIDO A EXPENDEDORA FI****\n')
    
    def mensaje_despedida():
        print('\n****GRACIAS VUELVA PRONTO ****')

    

    
class Bebidas: 
    def __init__(self,nombrerefresco,precio,caducidad,codigo,piezas):
        self.nombrerfresco=nombrerefresco
        self.precio=float(precio)
        self.caducidad=caducidad
        self.codigo=float(codigo)
        self.piezas=float(piezas)   


respuesta=None 
Eleccion=None
respuesta2=None
listaRefrescos=Bebidas('Coca-Cola',20,'20 de noviembre de 2025',400,10)
listaRefrescos2=Bebidas('Pepsi',16,'3 de octubre de 2025',500,10)
listaRefrescos3=Bebidas('Zenzao',15,'3 de enero de 2024',600,10)
listajugos=Bebidas('Boing de mango',20,'30 de octubre de 2024',700,)
listajugos=Bebidas('Jumex de Piña',)
listajugos=Bebidas('')
listajugos=Bebidas('')
listajugos=Bebidas('')
listajugos=Bebidas('')
listajugos=Bebidas('')
listajugos=Bebidas('')
listaJugos=Bebidas('Boing de mango','Jumex de Piña','Tutti de Durazno')
listaMineral=Bebidas('Peñafiel Natural','Peñafiel de limón','Topo-Chico')

while respuesta != 0 :
            try:
                respuesta=int(input('Favor de ingresar una Opción (Solo Números):\n1.Mostrar y Escoger Productos\n2.Quitar golosinas\n3.Pagar\4.Salir\n'))
                #respuesta = respuesta  
        
                if respuesta == 1 :
                    Eleccion=int(input('Porfavor elige tus Productos:\n1.Bebidas\2.Golo'))

                    if Eleccion ==1:
                        print('Nuestros refrescos disponibles son los siguientes:\n',listaJugos.nombrerfresco)
                             
                    elif Eleccion==2: 
                        print('Perame tantito carnal')

                    
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
                    print('\n****GRACIAS VUELVA PRONTO ****')
                
            except: 
                print('Opcion Invalida! SOLO PONER NUMEROS (SOLO NÚMEROS!!!!)')

            

menuprincipal()