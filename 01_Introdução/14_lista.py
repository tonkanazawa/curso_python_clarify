"""
Listas
Em outras linguagens é conhecida como Array, Vetor ou matriz...

* Dinâmica >>> Não possui tamanho fixo e não preciso informar este tamanho.
* Aceita qualquer tipo de dado.

* Sintaxe:
        [] ou list()

* SORT >>> Ordena os dados de uma lista.
* REVERSE >>> Inverte a lista.
* APPENDD >>> Atribui a lista, um elemento por vez. Podendo ser inclusive outra lista...
* INSERT >>> Atribui vários elementos, integrando à lista original.
* POP >>> Remove um valor da lista por índice.
* REMOVE >>> Remove um valor da lista por valor.
* ENUMERATE >>> Acesso à chave e valor.
* SHALLOW COPY
* CLEAR >>> Limpa a lista.
"""
# n10 = list(range(0,101,10))
# print(n10)

# notas = []

# for n in range(4):
#     notas.append(float(input('Nota: ')))

# notas.sort()
# print(notas)

notas = [50,100,20,350,40]
print(notas)
notas.sort()
print(notas)
notas.pop(3)
print(notas)
notas.append(4)
print(notas)
notas.insert(1, 24)
print(notas)
notas.remove(20)
print(notas)