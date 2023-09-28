"""
Dicionários - Em outras linguagens, conhecido como MAPA.

Sintaxe
exemplo1 = {}
exemplo2 = dict()

Aceita qualquer tipo de dado.
As chaves não podem ser repetidas.
"""

tupla1 = ()
tupla2 = tuple()

lista1 = []
lista2 = list()

dicionario = {}
dicionario2 = dict()

paises1 = {'br': 'Brasil'}
paises2 = dict(br = 'Brasil')  

paises = dict(
    br = 'Brasil',
    py = 'Paraguai',
    ar = 'Argentina'
)

print(paises)
paises['us'] = 'Estados Unidos'
print(paises)

paises['br'] = "Leo"
print(paises)

paises.update({'us', 'Estados desUnidos'})
print(paises)