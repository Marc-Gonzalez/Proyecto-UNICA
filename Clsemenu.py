def menuprincipal():
    def mensaje_bienvenida():

        print('****BIENVENIDO A EXPENDEDORA FI****\n')
    
    def mensaje_despedida():
        print('\n****GRACIAS VUELVA PRONTO ****')

    

catalogo_precios = {"Coca-Cola": 20, "Pepsi": 16,'Zenzao':15,'Boing de mango':20,'Jumex de Piña':25,'Tutti de durazno':30,'Pelafiel de mango':19,'Peñafiel delimon':22,'Topo-Chico':33}
carrito = {}

carrito["Coca-Cola"] = 20
carrito["Ppesi"] = 26
carrito["Zenzao"] = 15
carrito["Boing de Mango"] = 20
carrito["Jumex de Piña"] = 25
carrito["Tutti de durazno"] = 30
carrito["Peñafiel de Mango"] = 19
carrito["Peñafiel de limon"] = 22
carrito["Topo-Chico"] = 33




    
class Bebidas: 
    def __init__(self,nombrerefresco,precio,caducidad,codigo,piezas):
        self.nombrerfresco=nombrerefresco
        self.precio=float(precio)
        self.caducidad=caducidad
        self.codigo=float(codigo)
        self.piezas=float(piezas)

    def agregar(self, cantidad):
        self.piezas += cantidad

    def vender(self, cantidad):
        self.piezas -= cantidad

    def almacen(self):
        return self.piezas
    
    def getPrecio(self):
        return self.precio
class Refrescos(Bebidas):
     def __init__(self,nombrerefresco,precio,caducidad,codigo,piezas)->int:
          super().__init__ (nombrerefresco,precio,caducidad,codigo,piezas)

class jugos(Bebidas):
     def __init__(self,nombrerefresco,precio,caducidad,codigo,piezas)->int:
          super().__init__ (nombrerefresco,precio,caducidad,codigo,piezas)

class agua(Bebidas):
      def __init__(self,nombrerefresco,precio,caducidad,codigo,piezas)->int:
          super().__init__ (nombrerefresco,precio,caducidad,codigo,piezas)
          pass 
     


respuesta=None 
Eleccion=None
respuesta2=None
Refrescos1=Bebidas('---Coca-Cola---',20, '------20 de noviembre de 2025------',400,10)
Refrescos2=Bebidas('---Pepsi---',16,'------3 de octubre de 2025-----------',500,10)
Refrescos3=Bebidas('---Zenzao---',15,'------3 de enero de 2024-------------',600,10)
jugos1=Bebidas('---Boing de mango---',20,'------30 de octubre de 2024-------',700,20)
jugos2=Bebidas('---Jumex de Piña---',25,'------30 de enero de 2030-------',800,20)
jugos3=Bebidas('---Tutti de Durazno---',30,'------25 de febrero de 2023------',900,25)
Aguas1=Bebidas('---Peñafiel de mango---',19,'------26 de marzo de 2022------',1000,30)
Aguas2=Bebidas('---Peñafiel de limon---',22,'------26 de abril de 2025------',1100,20)
Aguas3=Bebidas('---Topo-Chico---',33,'-----28 de febrero de 2026-------',1200,10)

almacen={'---Coca-Cola---':Refrescos1,'---Pepsi---':Refrescos2,'---Zenzao---':Refrescos3,
         '---Boing de mango---':jugos1,'---Jumex de piña---':jugos2,'---Tutti de durazno---':jugos3,
         '---Peñafiel de mango---':Aguas1,'---Peñafiel de limon---':Aguas2,'---Topo-Chico---':Aguas3}

while respuesta != 0 :
            try:
                respuesta=int(input('Favor de ingresar una Opción (Solo Números):\n1.Mostrar y Escoger Productos\n2.Quitar golosinas\n3.Pagar\n4.Salir\n'))
                respuesta = respuesta  
        
                if respuesta == 1 :
                    Eleccion=int(input('Porfavor elige tus Productos:\n1.Bebidas\n2.Golosinas\n'))
                    if Eleccion == 1:
                        print('Nuestras Bebidas disponibles son los siguientes:\n')
                        for Chescos in almacen:
                         print(almacen[Chescos].precio,almacen[Chescos].piezas,almacen[Chescos].caducidad,almacen[Chescos].codigo)
                        
                        Eleccion2=float(input('Porfavor Ingrese el código de la Bebida que desea: \n'))
                        for Chescos in almacen: 
                            if Eleccion2==almacen[Chescos].codigo:
                                print({almacen[Chescos].codigo:[almacen[Chescos].precio,almacen[Chescos].caducidad,almacen[Chescos].piezas]})
                                Op=int(input('\n1.¿Cuántas piezas desea llevar?\n'))
                                almacen[Chescos].vender(Op)
                                print('Disponibles: ',almacen[Chescos].almacen())
                                print(f'Precio total: $ { Op * almacen[Chescos].getPrecio()}')

                            
                            


                        try:     
                            desicion=int(input('¿Desea agregar más cosas(FAVOR DE SOLO AGREGAR NÚMEROS): \n1.SI\n2.NO\n'))
                                
                        
                            if desicion == 2 :
                                print('\n****GRACIAS VUELVA PRONTO ****')
                                menuprincipal()
                               
                             
                        except: 
                            print('Opcion Invalida! SOLO PONER NUMEROS (SOLO NÚMEROS!!!!)')
                                     
                           

                    elif Eleccion2==almacen[Chescos].codigo:
                        for Chescos in almacen: 
                             print({almacen[Chescos].codigo:[almacen[Chescos].precio,almacen[Chescos].caducidad,almacen[Chescos].piezas]})
                             Op=int(input('\n1.¿Cuántas piezas desea llevar?\n'))
                             almacen[Chescos].vender(Op)
                             print('Disponibles: ',almacen[Chescos].almacen())
                             print(f'Precio total: $ { Op * almacen[Chescos].getPrecio()}')

                        try:     
                            desicion=int(input('¿Desea agregar más cosas(FAVOR DE SOLO AGREGAR NÚMEROS): \n1.SI\n2.NO\n'))
                                
                        
                            if desicion == 2 :
                                print('\n****GRACIAS VUELVA PRONTO ****')
                                menuprincipal()
                               
                             
                        except: 
                            print('Opcion Invalida! SOLO PONER NUMEROS (SOLO NÚMEROS!!!!)')
                            
                            

                    elif Eleccion2==almacen[Chescos].codigo:
                        for Chescos in almacen:
                             print({almacen[Chescos].codigo:[almacen[Chescos].precio,almacen[Chescos].caducidad,almacen[Chescos].piezas]})
                             Op=int(input('\n1.¿Cuántas piezas desea llevar?\n'))
                             almacen[Chescos].vender(Op)
                             print('Disponibles: ',almacen[Chescos].almacen())
                             print(f'Precio total: $ { Op * almacen[Chescos].getPrecio()}')
                        try:     
                            desicion=int(input('¿Desea agregar más cosas(FAVOR DE SOLO AGREGAR NÚMEROS): \n1.SI\n2.NO\n'))
                                
                        
                            if desicion == 2 :
                                print('\n****GRACIAS VUELVA PRONTO ****')
                                menuprincipal()
                               
                             
                        except: 
                            print('Opcion Invalida! SOLO PONER NUMEROS (SOLO NÚMEROS!!!!)')
                             

                    elif Eleccion2==almacen[Chescos].codigo:
                        for Chescos in almacen:
                             print({almacen[Chescos].codigo:[almacen[Chescos].precio,almacen[Chescos].caducidad,almacen[Chescos].piezas]})
                             Op=int(input('\n1.¿Cuántas piezas desea llevar?\n'))
                             almacen[Chescos].vender(Op)
                             print('Disponibles: ',almacen[Chescos].almacen())
                             print(f'Precio total: $ { Op * almacen[Chescos].getPrecio()}')
                        try:     
                            desicion=int(input('¿Desea agregar más cosas(FAVOR DE SOLO AGREGAR NÚMEROS): \n1.SI\n2.NO\n'))
                                
                        
                            if desicion == 2 :
                                print('\n****GRACIAS VUELVA PRONTO ****')
                                menuprincipal()
                               
                             
                        except: 
                            print('Opcion Invalida! SOLO PONER NUMEROS (SOLO NÚMEROS!!!!)')
                             



                    elif Eleccion2==almacen[Chescos].codigo:
                        for Chescos in almacen:
                             print({almacen[Chescos].codigo:[almacen[Chescos].precio,almacen[Chescos].caducidad,almacen[Chescos].piezas]})
                             Op=int(input('\n1.¿Cuántas piezas desea llevar?\n'))
                             almacen[Chescos].vender(Op)
                             print('Disponibles: ',almacen[Chescos].almacen())
                             print(f'Precio total: $ { Op * almacen[Chescos].getPrecio()}')
                        try:     
                            desicion=int(input('¿Desea agregar más cosas(FAVOR DE SOLO AGREGAR NÚMEROS): \n1.SI\n2.NO\n'))
                                
                        
                            if desicion == 2 :
                                print('\n****GRACIAS VUELVA PRONTO ****')
                                menuprincipal()
                               
                             
                        except: 
                            print('Opcion Invalida! SOLO PONER NUMEROS (SOLO NÚMEROS!!!!)')


                    elif Eleccion2==almacen[Chescos].codigo:
                        for Chescos in almacen:
                             
                             print({almacen[Chescos].codigo:[almacen[Chescos].precio,almacen[Chescos].caducidad,almacen[Chescos].piezas]})
                             Op=int(input('\n1.¿Cuántas piezas desea llevar?\n'))
                             almacen[Chescos].vender(Op)
                             print('Disponibles: ',almacen[Chescos].almacen())
                             print(f'Precio total: $ { Op * almacen[Chescos].getPrecio()}')
                        try:     
                            desicion=int(input('¿Desea agregar más cosas(FAVOR DE SOLO AGREGAR NÚMEROS): \n1.SI\n2.NO\n'))
                                
                        
                            if desicion == 2 :
                                print('\n****GRACIAS VUELVA PRONTO ****')
                                menuprincipal()
                               
                             
                        except: 
                            print('Opcion Invalida! SOLO PONER NUMEROS (SOLO NÚMEROS!!!!)')
                             

                    elif Eleccion2==almacen[Chescos].codigo:
                        for Chescos in almacen:
                             
                             print({almacen[Chescos].codigo:[almacen[Chescos].precio,almacen[Chescos].caducidad,almacen[Chescos].piezas]})
                             Op=int(input('\n1.¿Cuántas piezas desea llevar?\n'))
                             almacen[Chescos].vender(Op)
                             print('Disponibles: ',almacen[Chescos].almacen())
                             print(f'Precio total: $ { Op * almacen[Chescos].getPrecio()}')
                        try:     
                            desicion=int(input('¿Desea agregar más cosas(FAVOR DE SOLO AGREGAR NÚMEROS): \n1.SI\n2.NO\n'))
                                
                        
                            if desicion == 2 :
                                print('\n****GRACIAS VUELVA PRONTO ****')
                                menuprincipal()
                               
                             
                        except: 
                            print('Opcion Invalida! SOLO PONER NUMEROS (SOLO NÚMEROS!!!!)')
                             
                          

                    elif Eleccion2==almacen[Chescos].codigo:
                        for Chescos in almacen:
                             print({almacen[Chescos].codigo:[almacen[Chescos].precio,almacen[Chescos].caducidad,almacen[Chescos].piezas]})
                             Op=int(input('\n1.¿Cuántas piezas desea llevar?\n'))
                             almacen[Chescos].vender(Op)
                             print('Disponibles: ',almacen[Chescos].almacen())
                             print(f'Precio total: $ { Op * almacen[Chescos].getPrecio()}')
                        try:     
                            desicion=int(input('¿Desea agregar más cosas(FAVOR DE SOLO AGREGAR NÚMEROS): \n1.SI\n2.NO\n'))
                                
                        
                            if desicion == 2 :
                                print('\n****GRACIAS VUELVA PRONTO ****')
                                menuprincipal()
                               
                             
                        except: 
                            print('Opcion Invalida! SOLO PONER NUMEROS (SOLO NÚMEROS!!!!)')
                             
                        
                    elif Eleccion2==almacen[Chescos].codigo:
                        for Chescos in almacen:
                             
                             print({almacen[Chescos].codigo:[almacen[Chescos].precio,almacen[Chescos].caducidad,almacen[Chescos].piezas]})
                             Op=int(input('\n1.¿Cuántas piezas desea llevar?\n'))
                             almacen[Chescos].vender(Op)
                             print('Disponibles: ',almacen[Chescos].almacen())
                             print(f'Precio total: $ { Op * almacen[Chescos].getPrecio()}')
                        try:     
                            desicion=int(input('¿Desea agregar más cosas(FAVOR DE SOLO AGREGAR NÚMEROS): \n1.SI\n2.NO\n'))
                                
                        
                            if desicion == 2 :
                                print('\n****GRACIAS VUELVA PRONTO ****')
                                menuprincipal()
                               
                             
                        except: 
                            print('Opcion Invalida! SOLO PONER NUMEROS (SOLO NÚMEROS!!!!)')
                             
                        


                    elif Eleccion==2: 
                        print('Perame tantito carnal')

                    
                    continue
                
                elif respuesta==2:
                    print('aquie metemos una función que quite las golosinas\n')
                    continue
                elif respuesta==3:
                    print('Tu total a pagar es: \n',Total_a_Pagar,Total_Piezas) #Aquí hay que meter código para cobrar
                    
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