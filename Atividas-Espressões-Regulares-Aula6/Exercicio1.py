'''Ok, segue mais alguns exercicios para serem resolvidos com python 1. Validação de CPF Crie uma expressão regular em Python que valide um CPF no formato 000.000.000-00.Resposta: import re # Expressão regular para CPF no formato 000.000.000-00 padrao_cpf = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'''

import re

# Expressão regular para CPF no formato 000.000.000-00
padrao_cpf = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'

def validar_cpf(cpf: str) -> bool:
    """Valida o formato de um CPF no padrão 000.000.000-00"""
    return re.match(padrao_cpf, cpf) is not None


# Exemplos de teste
cpfs = [
    "123.456.789-00",  # válido
    "111.222.333-44",  # válido
    "12345678900",     # inválido
    "12.3456.789-00",  # inválido
    "123.456.789.00"   # inválido
]

print("=== Validação de CPF ===\n")
for cpf in cpfs:
    print(f"{cpf:15} → {'✅ válido' if validar_cpf(cpf) else '❌ inválido'}")
