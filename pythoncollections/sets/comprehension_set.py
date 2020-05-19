set_coprehension = { i * i for i in range (0, 10)}
set_1 = {1,2}
set_2 = {3,4}
print(set_coprehension)
set_coprehension = { i for i in set_1.union(set_2)}
print(set_coprehension)