#Su principal funcionalidad es tener elementos únicos, si en un set se encuentra un elemento duplicado, este es removido.
#Se pueden declarar con la palabra set o directamente con llaves. 
#Son inmutables, y no se pueden agregar tipos de listas o diccionarios.
#Los sets solo esperan 1 solo argumento, por eso siempre debben ir agrupados con [] o {}
mi_set = set([1,2,3,4,5])
print(mi_set, type(mi_set))

otro_set = {1,2,4}
print(otro_set, type(otro_set))

#elementos únicos
mi_set = set([1,2,5,2,3,4,5])
print(mi_set, type(mi_set))