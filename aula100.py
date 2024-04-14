import copy

from dados import produtos

# Exercícios
# Aumente o preço dos produto em 10 por cento
# Gere novos_produtos por deep copy(cópia continua)
novos_produtos = [
    {**p, 'preço': round(p['preço'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]

# print(*produtos, sep='\n')
# print("=" * 20)
# print(*novos_produtos, sep='\n')

# Ordene os produtos por nome decrescente(do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy(cópia profunda)

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)

# print(*produtos, sep='\n')
# print("=" * 20)
# print(*produtos_ordenados_por_nome, sep='\n')
# Ordene os produtos por nome crescente(do meno para maior)
# Gere produtos_ordenados_por_preco por deep copy(cópia profunda)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preço'],
    reverse=True
)

# print(*produtos, sep='\n')
# print("=" * 20)
# print(*produtos_ordenados_por_preco, sep='\n')

# FINAL

print(*produtos, sep='\n')
print("=" * 20)
print(*novos_produtos, sep='\n')
print("=" * 20)
print(*produtos_ordenados_por_nome, sep='\n')
print("=" * 20)
print(*produtos_ordenados_por_preco, sep='\n')
