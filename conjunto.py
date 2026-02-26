A = [1, 2, 3]
B = [2, 3, 4]
uniao = list(set(A + B))
interseçao = [x for x in A if x in B]
print(f"A = {A}")
print(f"B = {B}")
print(f"União: {uniao}")
print(f"Interseção: {interseçao}")
