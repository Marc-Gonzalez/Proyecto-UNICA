def menuprincipal():
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
Refrescos1=Bebidas('Coca-Cola',20,'20 de noviembre de 2025',400,10)
Refrescos2=Bebidas('Pepsi',16,'3 de octubre de 2025',500,10)
Refrescos3=Bebidas('Zenzao',15,'3 de enero de 2024',600,10)
jugos1=Bebidas('Boing de mango',20,'30 de octubre de 2024',700,20)
jugos2=Bebidas('Jumex de Piña',25,'30 de enero de 2030',800,20)
jugos3=Bebidas('Tutti de Durazno',30,'25 de febrero de 2023',900,25)
Aguas1=Bebidas('Peñafiel de mango',19,'26 de marzo de 2022',1000,30)
Aguas2=Bebidas('Peñafiel de limon',22,'26 de abril de 2025',1100,20)
Aguas3=Bebidas('Topo-Chico',33,'28 de febrero de 2026',1200,10)

almacen={'Coca-Cola':Refrescos1,'Pepsi':Refrescos2,'Zenzao':Refrescos3,
         'Boing de mango':jugos1,'Jumex de piña':jugos2,'Tutti de durazno':jugos3,
         'Peñafiel de mango':Aguas1,'Peñafiel de limon':Aguas2,'Topo-Chico':Aguas3}

while respuesta != 0 :
            try:
                respuesta=int(input('Favor de ingresar una Opción (Solo Números):\n1.Mostrar y Escoger Productos\n2.Quitar golosinas\n3.Pagar\n4.Salir\n'))
                respuesta = respuesta  
        
                if respuesta == 1 :
                    Eleccion=int(input('Porfavor elige tus Productos:\n1.Bebidas\n2.Golosinas\n'))
                        #¿COMO AGREGO SALTOS DE LÍNEAS?
                    if Eleccion == 1:
                        print('Nuestras Bebidas disponibles son los siguientes:\n',[{Refrescos1.codigo:Refrescos1.nombrerfresco,Refrescos2.codigo:Refrescos2.nombrerfresco,
                                                                                       Refrescos3.codigo:Refrescos3.nombrerfresco,jugos1.codigo:jugos1.nombrerfresco,
                                                                                       jugos2.codigo:jugos2.nombrerfresco,jugos3.codigo:jugos3.nombrerfresco,
                                                                                       Aguas1.codigo:Aguas1.nombrerfresco,Aguas2.codigo:Aguas2.nombrerfresco,
                                                                                       Aguas3.codigo:Aguas3.nombrerfresco}])
                        
                        Eleccion2=float(input('Porfavor Ingrese el código de la Bebida que desea: \n'))
                        if Eleccion2==Refrescos1.codigo:
                             print({Refrescos1.codigo:[Refrescos1.precio,Refrescos1.caducidad,Refrescos1.piezas]})
                             Op=int(input('\n1.¿Cuántas piezas desea llevar?\n'))
                             almacen['Coca-Cola'].vender(Op)
                             print('Disponibles: ',almacen['Coca-Cola'].almacen())
                             print(f'Precio total: $ { Op * Refrescos1.getPrecio()}')

                        try:
                             
                             desicion=int(input('¿Desea agregar más cosas(FAVOR DE SOLO AGREGAR NÚMEROS): \n1.SI\n2.NO\n'))

                             while desicion != 1 or 2 : 
                                
                                if desicion ==1:
                                     def menuprincipal():
                                           menuprincipal()
                                elif desicion == 2:
                                     print('\n****GRACIAS VUELVA PRONTO ****')
                                     menuprincipal()
                               
                             
                        except: 
                                print('Opcion Invalida! SOLO PONER NUMEROS (SOLO NÚMEROS!!!!)')
                            

                                     
                           

                    elif Eleccion2==Refrescos2.codigo:
                             print({Refrescos2.codigo:[Refrescos2.precio,Refrescos2.caducidad,Refrescos2.piezas]})
                             Op=int(input('\n1.¿Cuántas piezas desea llevar?\n'))
                             almacen['Ppesi'].vender(Op)
                             print('Disponibles: ',almacen['Pepsi'].almacen())
                             print(f'Precio total: $ { Op * Refrescos2.getPrecio()}')
                            

                    elif Eleccion2==Refrescos3.codigo:
                             print({Refrescos3.codigo:[Refrescos3.precio,Refrescos3.caducidad,Refrescos3.piezas]})
                             Op=int(input('\n1.¿Cuántas piezas desea llevar?\n'))
                             almacen['Zenzao'].vender(Op)
                             print('Disponibles: ',almacen['Zenzao'].almacen())
                             print(f'Precio total: $ { Op * Refrescos3.getPrecio()}')
                             

                    elif Eleccion2==jugos1.codigo:
                             print({jugos1.codigo:[jugos1.precio,jugos1.caducidad,jugos1.piezas]})
                             Op=int(input('\n1.¿Cuántas piezas desea llevar?\n'))
                             almacen['Boing de mango'].vender(Op)
                             print('Disponibles: ',almacen['Boing de mango'].almacen())
                             print(f'Precio total: $ { Op * jugos1.getPrecio()}')
                             print(f'Precio total: $ { Op * jugos1.getPrecio()}')

                    elif Eleccion2==jugos2.codigo:
                             print({jugos2.codigo:[jugos2.precio,jugos2.caducidad,jugos2.piezas]})
                             Op=int(input('\n1.¿Cuántas piezas desea llevar?\n'))
                             almacen['Jumex de Piña'].vender(Op)
                             print('Disponibles: ',almacen['Jumex de Piña'].almacen())
                             print(f'Precio total: $ { Op * jugos2.getPrecio()}')
                             print(f'Precio total: $ { Op * jugos2.getPrecio()}')

                    elif Eleccion2==jugos3.codigo:
                             print({jugos3.codigo:[jugos3.precio,jugos3.caducidad,jugos3.piezas]})
                             Op=int(input('\n1.¿Cuántas piezas desea llevar?\n'))
                             almacen['Tutti de durazno'].vender(Op)
                             print('Disponibles: ',almacen['Tutti de durazno'].almacen())
                             print(f'Precio total: $ { Op * jugos3.getPrecio()}')
                             

                    elif Eleccion2==Aguas1.codigo:
                             print({Aguas1.codigo:[Aguas1.precio,Aguas1.caducidad,Aguas1.piezas]})
                             Op=int(input('\n1.¿Cuántas piezas desea llevar?\n'))
                             almacen['Peñafiel de mango'].vender(Op)
                             print('Disponibles: ',almacen['Peñafiel de mango'].almacen())
                             print(f'Precio total: $ { Op * Aguas1.getPrecio()}')
                             
                          

                    elif Eleccion2==Aguas2.codigo:
                             print({Aguas2.codigo:[Aguas2.precio,Aguas2.caducidad,Aguas2.piezas]})
                             Op=int(input('\n1.¿Cuántas piezas desea llevar?\n'))
                             almacen['Peñafiel de limon'].vender(Op)
                             print('Disponibles: ',almacen['Peñafiel de limon'].almacen())
                             print(f'Precio total: $ { Op * Aguas2.getPrecio()}')
                            
                        
                    elif Eleccion2==Aguas3.codigo:
                             print({Aguas1.codigo:[Aguas3.precio,Aguas3.caducidad,Aguas3.piezas]})
                             Op=int(input('\n1.¿Cuántas piezas desea llevar?\n'))
                             almacen['Topo-Chico'].vender(Op)
                             print('Disponibles: ',almacen['Topo-Chico'].almacen())
                             print(f'Precio total: $ { Op * Aguas3.getPrecio()}')
                             
                        


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