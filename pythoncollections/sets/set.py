# DECLARAÇÃO DE UM SET

meu_set = {1,2,3,4,1}
meu_set_2 = {2,3,4,5,6,7,8,9,10,11,12,13}

# ADICIONANDO

meu_set.add(5)
print(meu_set)

#update
meu_set.update([3,4,5,7,8,9,10])
print(meu_set)

#discard
meu_set.discard(7)
print(meu_set)

#união
print(meu_set | meu_set_2)
print(meu_set.union(meu_set_2))

#Interseção
print(meu_set & meu_set_2)
print(meu_set.intersection(meu_set_2))

#Diferença
print(meu_set - meu_set_2)
print(meu_set.difference(meu_set_2))

#Diferença Simétrica
print(meu_set ^ meu_set_2)
print(meu_set.symmetric_difference(meu_set_2))