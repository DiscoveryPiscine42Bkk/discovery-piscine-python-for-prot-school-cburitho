arrays = [2,4,6,8,10,12,14]
n_a = [x + 2 for x in arrays if x > 5]
n_a2 = list(set(n_a))

print(arrays)
print(n_a2)