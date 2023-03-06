
class golosinas:
    def __init__(self,codigo, dulce, precio, caducidad, piezas) -> int:
        self.codigo = float(codigo)
        self.dulce = dulce
        self.precio = int(precio)
        self.caducidad = caducidad
        self.piezas = int(piezas)
    
    def almacen(self):
        return self.piezas

    def agregar(self,cantidad):
        self.piezas +=  cantidad

    def vender(self, cantidad):
        self.piezas -= cantidad
        
    def getPrecio(self):
        return self.precio



class paletas(golosinas):
    def __init__(self, codigo,dulce, precio, caducidad, piezas) -> int:
        super().__init__(codigo,dulce, precio, caducidad, piezas)

class chocolates(golosinas):
    def __init__(self, codigo, dulce, precio, caducidad, piezas) -> int:
        super().__init__(codigo, dulce, precio, caducidad, piezas)
    pass


buba = paletas(1,'bubbalob',2,'10 diciembre 2023', 1000)
rocka = paletas(1.1,'rockaleta',3,'10 diciembre 2023', 1000)
sonrics = paletas(1.2,'sonricks',4,'10 diciembre 2023', 1000)

carlosv = chocolates(2,'carlosv',8,'11 noviembre',600)
ferrero = chocolates(2.1,'ferrero Roshe',20,'11 noviembre',600)
lapose = chocolates(2.2,'Lapose',7,'11 noviembre',600)

almacen = {'bubbalob' : buba,'rockaleta': rocka,'sonrics':sonrics,'carlosv': carlosv,'ferrero Roshe':ferrero,'Lapose':lapose}
while(True):
    try:
        listadedulces = int(input('\n\n\tescoger la categoria de dulces:\n\n\t1.paletas\n\n\t2.chocolates\n\n\t3.Mostrar almacen disponible\n\n\t4.Salir\n'))

        if listadedulces == 1:
            print('\n\n\tlista de paletas: \n\n\t',[{buba.codigo:buba.dulce,rocka.codigo: rocka.dulce,sonrics.codigo: buba.dulce}])

            op2 = float(input('\n\tingrese el codigo de paleta\n\n\n\t'))
                        
            if op2 == buba.codigo :
                while(True):
                    try:
                        print({buba.codigo: [buba.dulce,buba.precio,buba.caducidad,buba.piezas]})
                        operacion = int(input('\n1.Mostrar Golosinas\n2.Vender golosinas\n3.Pagar\n4.Salirn\n5.elige otro numero para volver añadir al carrito\n'))
                        
                        if operacion== 1 :  
                            print({buba.codigo: [buba.dulce,buba.precio,buba.caducidad,buba.piezas]})
                            continue  
                        elif operacion == 2 :
                            x = int(input('numero de dulces '))
                            almacen['bubbalob'].vender(x)
                            print(almacen['bubbalob'].almacen())
                            continue
                        elif operacion == 3:
                            print(f'Precio total: $ { x * buba.getPrecio()}')
                            continue     
                        elif operacion == 4:
                            print('salir')
                            break
                    except:
                        print('\n\tSOLO NUMEROS \n\t')
            
            elif op2 == rocka.codigo :
                while(True):
                    try:
                        print({rocka.codigo: [rocka.dulce,rocka.precio,rocka.caducidad,rocka.piezas]})
                        operacion = int(input('\n1.Mostrar Golosinas\n2.Vender golosinas\n3.Pagar\n4.Salirn\n'))                        
                        if operacion== 1 :  
                            print(almacen['rockaleta'].almacen())
                            continue  
                        elif operacion == 2 :
                            x = int(input('numero de dulces '))
                            almacen['rockaleta'].vender(x)
                            print(almacen['rockaleta'].almacen())
                            continue
                        elif operacion == 3:
                            print(f'Precio total: $ { x * rocka.getPrecio()}')
                            continue
                        elif operacion == 4:
                            print('salir')
                            break
                        elif operacion == 5:
                            print('AGREGUEMOS COSAS AL CARRITO')
                        continue
                    except:
                        print('\n\tSOLO NUMEROS \n\t')
            elif op2 == sonrics.codigo :
                while(True):
                    try:
                        print({sonrics.codigo: [sonrics.dulce,sonrics.precio,sonrics.caducidad,sonrics.piezas]})
                        operacion = int(input('\n1.Mostrar Golosinas\n2.Vender golosinas\n3.Pagar\n4.Salirn\n'))                         
                        if operacion== 1 :  
                            print(almacen['sonrics'].almacen())
                            continue  
                        elif operacion == 2 :
                            x = int(input('numero de dulces '))
                            almacen['sonrics'].vender(x)
                            print(almacen['sonrics'].almacen())
                            continue
                        elif operacion == 3:
                            print(f'Precio total: $ { x * sonrics.getPrecio()}')
                            continue
                        elif operacion == 4:
                            print('salir')
                            break
                    except:
                        print('\n\tSOLO NUMEROS \n\t')
    
        elif listadedulces == 2:
            
            print('\n\n\tlista de Chocolate: \n\n\t',[{carlosv.codigo:carlosv.dulce,ferrero.codigo: ferrero.dulce,lapose.codigo: lapose.dulce}])

            op3 = float(input('\n\tingrese el codigo de paleta\n\t'))
            if op3 == carlosv.codigo :
                while(True):
                    try:
                        print({carlosv.codigo: [carlosv.dulce,carlosv.precio,carlosv.caducidad,carlosv.piezas]})
                        operacion = int(input('\n1.Mostrar Golosinas\n2.Vender golosinas\n3.Pagar\n4.Salirn\n'))                         
                        if op3== 1 :  
                            print(almacen['carlosv'].almacen())
                            continue  
                        elif operacion == 2 :
                            x = int(input('numero de dulces '))
                            almacen['carlosv'].vender(x)
                            print(almacen['carlosv'].almacen())
                            continue
                        elif operacion == 3:
                            print(f'Precio total: $ { x * carlosv.getPrecio()}')
                            continue
                        elif operacion == 4:
                            print('salir')
                            break
                    except:
                        print('\n\tSOLO NUMEROS \n\t')
            elif op3 == ferrero.codigo :
                while(True):
                    try:
                        print({ferrero.codigo: [ferrero.dulce,ferrero.precio,ferrero.caducidad,ferrero.piezas]})
                        operacion = int(input('\n1.Mostrar Golosinas\n2.Vender golosinas\n3.Pagar\n4.Salirn\n'))                         
                        if op3== 1 :  
                            print(almacen['ferrero Roshe'].almacen())
                            continue  
                        elif operacion == 2 :
                            x = int(input('numero de dulces '))
                            almacen['ferrero Roshe'].vender(x)
                            print(almacen['ferrero Roshe'].almacen())
                            continue
                        elif operacion == 3:
                            print(f'Precio total: $ { x * ferrero.getPrecio()}')
                            continue
                        elif operacion == 4:
                            print('salir')
                            break
                    except:
                        print('\n\tSOLO NUMEROS \n\t')
            elif op3 == lapose.codigo :
                while(True):
                    try:
                        print({lapose.codigo: [lapose.dulce,lapose.precio,lapose.caducidad,lapose.piezas]})
                        operacion = int(input('\n1.Mostrar Golosinas\n2.Vender golosinas\n3.Pagar\n4.Salirn\n'))                         
                        if op3== 1 :  
                            print(almacen['Lapose'].almacen())
                            continue  
                        elif operacion == 2 :
                            x = int(input('numero de dulces '))
                            almacen['Lapose'].vender(x)
                            print(almacen['Lapose'].almacen())
                            continue
                        elif operacion == 3:
                            print(f'Precio total: $ { x * lapose.getPrecio()}')
                            continue
                        elif operacion == 4:
                            print('salir')
                            break
                    except:
                        print('\n\tSOLO NUMEROS \n\t')
            elif op3 == 3 :
                print('\SALIR\n')
        elif listadedulces == 3:
            for al in almacen:
                print({almacen[al].codigo: [almacen[al].dulce,almacen[al].precio,almacen[al].caducidad,almacen[al].piezas]})
        elif listadedulces == 4:
            print('\tSALIR DE GOLOSINAS\n')
            break
        else:
                print('no hay opciones')     
    except:
        print('------------------SOLO IMPRIME LOS NUMEROS POR FAVOR ----------')


# buba = paletas(1,'bubbalob',2,'10 diciembre 2023', 1000)
# rocka = paletas(1.1,'rockaleta',3,'10 diciembre 2023', 1000)
# sonrics = paletas(1.2,'sonricks',4,'10 diciembre 2023', 1000)

# carlosv = chocolates(2,'carlosv',8,'11 noviembre',600)
# ferrero = chocolates(2.1,'ferrero Roshe',20,'11 noviembre',600)
# lapose = chocolates(2.2,'Lapose',7,'11 noviembre',600)
catalogo_precios = {'chicle' : 2,'rockaleta': 3,'sonrics':4,'carlosv': 8,'ferrero Roshe':20,'Lapose':7}
carrito = {}
for precio in catalogo_precios:
#     # PRIMERA VEZ
#     #     carrito["rocaleta"] = 15
# #     EN CUALQUIER OTRO CASO

    carrito[almacen] = carrito['chicle'] + carrito['rockaleta'] + carrito['sonrics'] + carrito['carlosv'] + carrito['ferrero Roshe'] +  carrito['Lapose']
    carrito --> {'chicle' : 2,'rockaleta': 3,'sonrics':4,'carlosv': 8,'ferrero Roshe':20,'Lapose':7}
# #     CALCULAR EL PRECIO
    precio_total = carrito['chicle'] *buba[precio] + carrito['rockaleta'] + carrito['sonrics'] + carrito['carlosv'] + carrito['ferrero Roshe'] + carrito['Lapose']
