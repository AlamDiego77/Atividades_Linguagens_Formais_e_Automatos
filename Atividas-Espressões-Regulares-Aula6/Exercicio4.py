'''
4. Substituição de palavras Escreva um código que substitui todos os números de uma string por '#'. Resposta: import re texto = "Hoje é dia 17/09/2025 e o preço é 150 reais."
'''

import re

# Texto de exemplo
texto = "Hoje é dia 17/09/2025 e o preço é 150 reais."

# Substituir todos os dígitos por '#'
resultado = re.sub(r'\d', '#', texto)

print("=== Substituição de Números ===")
print(resultado)
