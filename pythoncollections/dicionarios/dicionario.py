meu_diionario = {1 : 'Fabio', 2: 'Maria', 3 : 'José'}
print(type(meu_diionario))
print(meu_diionario[3])
usuarios = { 10000: 'Joao Victor Lopes dos santos'}
print(usuarios[10000])

for chave, valor in meu_diionario.items():
    print(valor)

#get()
print(meu_diionario.get(2))

#len()
print(len(meu_diionario))

#pop()
meu_diionario.pop(2)
print(meu_diionario)

#clear()
meu_diionario.clear()
print(meu_diionario)

#keys
meu_diionario = {1 : 'Fabio', 2: 'Maria', 3 : 'José'}
print(meu_diionario.keys())

#Adicionando Elementos
meu_diionario[4] = 'Joaquina'
print(meu_diionario)