# # Sets
# conjunto1 = {'Leo', 2,5,7,9,8,10,'Milton'}
# conjunto2 = set()


# numeros = {5,6,1,5,1,8,1,6,8,1,8,6,1,6,8,4,6,5,1,6,7,9,2,3,'Milton'}
# print(numeros)
# numeros.add(200)
# print(numeros)
# numeros.pop()
# print(numeros)
# numeros.discard(4)
# print(numeros)
# numeros.remove(5)
# print(numeros)



# Analise cidades (cada pessoa que entrou colocou a cidade de nascimento)
cidade = ['Rio de Janeiro', 'São Paulo', 'Juiz de Fora', 'Petrolina',
          'Salvador','Juiz de Fora', 'Rio de Janeiro', 'Petrolina',
          'Salvador', 'São Paulo', 'São Paulo', 'São Paulo',  'Juiz de Fora',
          'Rio de Janeiro', 'Petrolina', 'Rio de Janeiro', 'Salvador',
          'Juiz de Fora',  'Petrolina', 'Salvador', 'Rio de Janeiro',
          'Rio de Janeiro', 'Rio de Janeiro', 'Rio de Janeiro', 'São Paulo',
          'São Paulo', 'São Paulo', 'São Paulo', 'Rio de Janeiro',
          'Rio de Janeiro', 'Rio de Janeiro',  'São Paulo', 'Rio de Janeiro',
          'São Paulo', 'Rio de Janeiro', 'São Paulo']

# print(f'Total de pessoas: {len(cidade)}')

# print(f'Total de pesosas do RJ: {cidade.count("Rio de Janeiro")}')

# lista_cidade = set(cidade)
# print(lista_cidade)
# print(f'Total de cidades: {len(lista_cidade)}')


curso_python = {'Leo A', 'Maria', 'Juca', 'Paulo', 'Ana', 'Beto'}
curso_sql = {'Leo A', 'Pedro', 'Juca', 'Cris', 'Claudia', 'Roberto'}

total_alunos1 = curso_python.union(curso_sql)
total_alunos2 = curso_python | curso_sql

ambos_cursos1 = curso_python.intersection(curso_sql)
ambos_cursos2 = curso_python & curso_sql

so_python1 = curso_python.difference(curso_sql)
so_sql1 = curso_sql.difference(curso_python)

so_python2 = curso_python ^ curso_sql
so_sql2 = curso_sql ^ curso_python




print(f'QTD alunos PY......: {len(curso_python)}')
print(f'QTD alunos SQL.....: {len(curso_sql)}')
print(f'Total de Alunos....: {len(total_alunos1)}')
print(f'Alunos nos 2 cursos: {len(ambos_cursos2)}')
print(f'Alunos só em Python: {len(so_python1)}')
print(f'Alunos só em SQL...: {len(so_sql1)}')
