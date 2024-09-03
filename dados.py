INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K += 1
    SOMA += K

print(SOMA)
def pertence_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

# Exemplo de uso:
numero = 21
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
    import json

# Dados de faturamento diário
faturamento = [
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    # ... continua com os outros dias
    {"dia": 30, "valor": 8414.61}
]

# Filtra os dias com faturamento
valores = [dia["valor"] for dia in faturamento if dia["valor"] > 0]

# Menor e maior valor de faturamento
menor_valor = min(valores)
maior_valor = max(valores)

# Média mensal
media_mensal = sum(valores) / len(valores)

# Dias com faturamento acima da média
dias_acima_media = len([valor for valor in valores if valor > media_mensal])

print(f"Menor valor de faturamento: {menor_valor}")
print(f"Maior valor de faturamento: {maior_valor}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total_faturamento = sum(faturamento_estados.values())

for estado, valor in faturamento_estados.items():
    percentual = (valor / total_faturamento) * 100
    print(f"{estado}: {percentual:.2f}%")

def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

# Exemplo de uso:
string = "Exemplo"
string_invertida = inverter_string(string)
print(f"String original: {string}")
print(f"String invertida: {string_invertida}")
