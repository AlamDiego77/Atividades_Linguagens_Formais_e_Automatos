''' 
3. Filtragem de palavras com 3 letras Dada uma lista de palavras, use regex para filtrar apenas as que têm exatamente 3 letras (ex: sol, lua). Resposta: import re # Regex para palavras com exatamente 3 letras padrao = r'^[a-zA-Z]{3}$'
'''
import re

# Regex para palavras com exatamente 3 letras
padrao = r'^[a-zA-Z]{3}$'

# Lista de palavras
palavras = ["sol", "lua", "casa", "ar", "céu", "mar", "rio"]

# Filtrar com list comprehension
resultado = [p for p in palavras if re.match(padrao, p)]

print("=== Palavras com 3 letras ===")
print(resultado)
