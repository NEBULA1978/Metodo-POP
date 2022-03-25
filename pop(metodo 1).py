"""
sintaxis: list.pop()
metodo1
RETORNA:devuelve y elimina el ultimo elemento de
la lista

lista= ["mouse","teclado","monitor"]
hardware=lista.pop()
print(lista)
print(hardware)
"""


"""
metodo2 POP
sintaxis: list.pop(int)
RETORNA:devuelve y elimina el elemnto del indice int de la lista

lista= ["mouse","teclado","monitor"]
hardware=lista.pop(1)
hardware=lista.pop(0)
print(lista)
print(hardware)
"""

"""
remove
sintaxis: list.remove(elemento)
NO RETORNA,elimina elemento de la lista
solo si el elemento esta en la lista,sino esta me da error
lista=["mouse","teclado","monitor"]
lista.remove("mouse")
print(lista)

"""



"""
del
sintaxis: del lista
NO RETORN,elimina lista

lista=["mouse","teclado","monitor"]
del lista
print(lista)
nameError:name "lista" is no defined

"""

"""
sintaxis: del lista[int]
NO RETORNA,elimina elelemento del indice int
elimina por indice 0,1,2,3,etc
lista= ["mouse","teclado","monitor"]
del lista[2]
print(lista)

"""
"""
index
sintaxis: lista.index(elemento)
RETORNA: EL indice int de donde se encuentra elemento
para saber que indice tiene en la lista
lista= ["mouse","teclado","monitor"]
id=lista.index("mouse")
print(id)

"""
"""
count
sintaxis: lista.count(elemento)
Retorna:Un int que representalacantidad de veces que se encuentra ese
elemento en la lista:

lista=["mouse","mouse","monitor"]
cantidad=lista.count("mouse")
lista.reverse()#sintaxis:lista.reverse()NO RETORNA,invierte el ordende la lista
print(cantidad)
print(lista)#sale asi la lista.reverse['monitor', 'mouse', 'mouse']
"""

"""
sort
sintaxis: lista.sort()
NO RETORNA, ordena lalista de menor a mayor

lista1=[2,5,3,4,5,7]
lista=["kevin","Axell","Juan"]
lista.sort()
lista1.sort()
print(lista)
print(lista1)
"""
"""
ordenar lista de mayor a menor
"""
lista=[2,5,3,4,5,7]
lista.sort()
lista.reverse()
print(lista)