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

almacen = {'bubbalob' : buba,'rockaleta': rocka,'sonrics':sonrics,'carlosv': carlosv,'ferrero Roshe':ferrero}

listadedulces = int(input('\n\n\tescoger la categoria de dulces:\n\n\t1.paletas\n\n\t2.chocolates\n\n\t'))


if listadedulces == 1:
    print('\n\n\tlista de paletas: \n\n\t',[{buba.codigo:buba.dulce,rocka.codigo: rocka.dulce,sonrics.codigo: buba.dulce}])

    op2 = float(input('\n\tingrese el codigo de paleta\n\n\n\t'))
                
    if op2 == buba.codigo :
        print({buba.codigo: [buba.dulce,buba.precio,buba.caducidad,buba.piezas]})
        operacion = int(input('desa\n1. venta\n2. ver piezas restantes en almacen\n3. cuenta total de paletas vendidas'))
        x = int(input('numero de dulces '))
        if operacion== 1 :  
            almacen['bubbalob'].vender(x)
            print(almacen['bubbalob'].almacen())
        elif operacion == 2 :
            print(almacen['bubbalob'].almacen())
        elif operacion == 3:
            print(f'Precio total: $ { x * buba.getPrecio()}')

    elif op2 == rocka.codigo:
        print({rocka.codigo: [rocka.dulce,rocka.precio,rocka.caducidad,rocka.piezas]})
        operacion = int(input('desa\n1. venta\n2. ver piezas restantes en almacen\n3. cuenta total de paletas vendidas'))
        x = int(input('numero de dulces '))
        if operacion== 1 :  
            almacen['rockaleta'].vender(x)
            print(almacen['rockaleta'].almacen())
        elif operacion == 2 :
            print(almacen['rockaleta'].almacen())
        elif operacion == 3:
            print(f'Precio total: $ { x * rocka.getPrecio()}')
    elif op2 == sonrics.codigo:
        print({sonrics.codigo: [sonrics.dulce,sonrics.precio,sonrics.caducidad,sonrics.piezas]})
        operacion = int(input('desa\n1. venta\n2. ver piezas restantes en almacen\n3. cuenta total de paletas vendidas'))
        x = int(input('numero de dulces '))
        if operacion== 1 :  
            almacen['sonrics'].vender(x)
            print(almacen['sonrics'].almacen())
        elif operacion == 2 :
            print(almacen['sonrics'].almacen())
        elif operacion == 3:
            print(f'Precio total: $ { x * sonrics.getPrecio()}')
    else:
            print('no existe opcion')

elif listadedulces == 2:
    print('\n\n\tlista de Chocolate: \n\n\t',[{carlosv.codigo:carlosv.dulce,ferrero.codigo: ferrero.dulce,lapose.codigo: lapose.dulce}])

    op3 = float(input('\n\tingrese el codigo de paleta\n\t'))
    if op3 == carlosv.codigo :
        print({carlosv.codigo: [carlosv.dulce,carlosv.precio,carlosv.caducidad,carlosv.piezas]})
        operacion = int(input('desa\n1. venta\n2. ver piezas restantes en almacen\n3. cuenta total de paletas vendidas'))
        x = int(input('numero de dulces '))
        if operacion== 1 :  
            almacen['carlosv'].vender(x)
            print(almacen['carlosv'].almacen())
        elif operacion == 2 :
            print(almacen['carlosv'].almacen())
        elif operacion == 3:
            print(f'Precio total: $ { x * carlosv.getPrecio()}')
        

    elif op3 == ferrero.codigo:
        print({rocka.codigo: [ferrero.dulce,ferrero.precio,ferrero.caducidad,ferrero.piezas]})
        operacion = int(input('desa\n1. venta\n2. ver piezas restantes en almacen\n3. cuenta total de paletas vendidas'))
        x = int(input('numero de dulces '))
        if operacion== 1 :  
            almacen['ferrero Roshe'].vender(x)
            print(almacen['ferrero Roshe'].almacen())
        elif operacion == 2 :
            print(almacen['ferrero Roshe'].almacen())
        elif operacion == 3:
            print(f'Precio total: $ { x * ferrero.getPrecio()}')
        


    elif op3 == lapose.codigo:
        print({sonrics.codigo: [lapose.dulce,lapose.precio,lapose.caducidad,lapose.piezas]})
        operacion = int(input('desa\n1. venta\n2. ver piezas restantes en almacen\n3. cuenta total de paletas vendidas'))
        x = int(input('numero de dulces '))
        if operacion== 1 :  
            almacen['Lapose'].vender(x)
            print(almacen['Lapose'].almacen())
        elif operacion == 2 :
            print(almacen['Lapose'].almacen())
        elif operacion == 3:
            print(f'Precio total: $ { x * lapose.getPrecio()}')

    else:
            print('no existe opcion')
else:
        print('no hay opciones')     

 class golosinas:
     def _init_(self,codigo, dulce, precio, caducidad, piezas) -> int:
         self.codigo = float(codigo)
         self.dulce = dulce
         self.precio = int(precio)
         self.caducidad = caducidad
         self.piezas = int(piezas)

     def agregar(self, cantidad):
         self.piezas += cantidad

     def vender(self, cantidad):
         self.piezas -= cantidad

     def almacen(self):
         return self.piezas
    
     def getPrecio(self):
         return self.precio

 class paletas(golosinas):
     def _init_(self, codigo,dulce, precio, caducidad, piezas) -> int:
         super()._init_(codigo,dulce, precio, caducidad, piezas)

 class chocolates(golosinas):
     def _init_(self, codigo, dulce, precio, caducidad, piezas) -> int:
         super()._init_(codigo, dulce, precio, caducidad, piezas)
     pass


 buba = paletas(1,'bubbalob',2,'10 diciembre 2023', 1000)
 rocka = paletas(1.1,'reockaleta',3,'10 diciembre 2023', 1000)
 sonrics = paletas(1.2,'ronricks',4,'10 diciembre 2023', 1000)

 carlosv = chocolates(2,'Carlosv',8,'11 noviembre',600)
 ferrero = chocolates(2.1,'ferrero Roshe',20,'11 noviembre',600)
 lapose = chocolates(2.2,'Lapose',7,'11 noviembre',600)

 almacen = {'1.2': buba, 'rocaleta': rocka}

 cantidadDeDulcae = 3

 print(almacen[x].almacen())
 print(almacen['bubalo'].getPrecio())
 almacen['bubalo'].vender(3)
 print(almacen['bubalo'].almacen())

 print(f'Precio total: {cantidadDeDulcae * buba.getPrecio()}')





 listadedulces = int(input('\n\n\tescoger la categoria de dulces:\n\n\t1.paletas\n\n\t2.chocolates\n\n\t'))


 if listadedulces == 1:
    
     print('\n\n\tlista de paletas: \n\n\t',[{buba.codigo:buba.dulce,rocka.codigo: rocka.dulce,sonrics.codigo: buba.dulce}])

     op2 = float(input('\n\tingrese el codigo de paleta\n\n\n\t'))
                
     if op2 == buba.codigo :
         print({buba.codigo: [buba.dulce,buba.precio,buba.caducidad,buba.piezas]})
     elif op2 == rocka.codigo:
         print({rocka.codigo: [rocka.dulce,rocka.precio,rocka.caducidad,rocka.piezas]})
     elif op2 == sonrics.codigo:
         print({sonrics.codigo: [sonrics.dulce,sonrics.precio,sonrics.caducidad,sonrics.piezas]})
     else:
             print('no existe opcion')
                
 elif listadedulces == 2:
     print('\n\n\tlista de Chocolate: \n\n\t',[{carlosv.codigo:carlosv.dulce,ferrero.codigo: ferrero.dulce,lapose.codigo: lapose.dulce}])

     op3 = float(input('\n\tingrese el codigo de paleta\n\t'))
     if op3 == carlosv.codigo :

         print({carlosv.codigo: [carlosv.dulce,carlosv.precio,carlosv.caducidad,carlosv.piezas]})
          ingrese la cantidad de dulces
          vvariable x
         carlosv.vender(x)
          quieres quitar

     elif op3 == ferrero.codigo:
         print({rocka.codigo: [ferrero.dulce,ferrero.precio,ferrero.caducidad,ferrero.piezas]})

     elif op3 == lapose.codigo:
         print({sonrics.codigo: [lapose.dulce,lapose.precio,lapose.caducidad,lapose.piezas]})

     else:
             print('no existe opcion')
 else:
         print('no hay opciones')}

"""
    catalogo_precios = {"rocaleta": 10, "bubalo": 2}
    carrito = {}
    PRIMERA VEZ
        carrito["rocaleta"] = 15
    EN CUALQUIER OTRO CASO
        carrito["rocaleta"] = carrito["rocaleta"] + 8
    carrito -- > {"rocaleta": 15, "bubalo": 7}

    CALCULAR EL PRECIO
    precio_total = carrito["rocaleta"] * 10 + carrito["rocaleta"] * 2
"""
