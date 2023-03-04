class golosinas:
    def __init__(self,codigo, dulce, precio, caducidad, piezas) -> int:
        self.codigo = float(codigo)
        self.dulce = dulce
        self.precio = int(precio)
        self.caducidad = caducidad
        self.piezas = int(piezas)

class paletas(golosinas):
    def __init__(self, codigo,dulce, precio, caducidad, piezas) -> int:
        super().__init__(codigo,dulce, precio, caducidad, piezas)
        
    def agregar(self):
        print('Agregar cosas a la canasta')
        


class chocolates(golosinas):
    def __init__(self, codigo, dulce, precio, caducidad, piezas) -> int:
        super().__init__(codigo, dulce, precio, caducidad, piezas)
    pass

buba = paletas(1,'bubbalob',2,'10 diciembre 2023', 1000)
rocka = paletas(1.1,'reockaleta',3,'10 diciembre 2023', 1000)
sonrics = paletas(1.2,'ronricks',4,'10 diciembre 2023', 1000)

carlosv = chocolates(2,'Carlosv',8,'11 noviembre',600)
ferrero = chocolates(2.1,'ferrero Roshe',20,'11 noviembre',600)
lapose = chocolates(2.2,'Lapose',7,'11 noviembre',600)


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

    elif op3 == ferrero.codigo:
        print({rocka.codigo: [ferrero.dulce,ferrero.precio,ferrero.caducidad,ferrero.piezas]})

    elif op3 == lapose.codigo:
        print({sonrics.codigo: [lapose.dulce,lapose.precio,lapose.caducidad,lapose.piezas]})

    else:
            print('no existe opcion')
else:
        print('no hay opciones')     
