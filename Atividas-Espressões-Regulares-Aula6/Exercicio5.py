'''
5. Detecção de placas de veículos Valide se uma string corresponde ao padrão de placa brasileira tradicional (ABC-1234). Resposta: import re # Regex para placas no formato ABC-1234 padrao_placa = r'^[A-Z]{3}-\d{4}$'
'''

import re

# Regex para placas no formato ABC-1234
padrao_placa = r'^[A-Z]{3}-\d{4}$'

def validar_placa(placa: str) -> bool:
    """Valida se a string corresponde a uma placa brasileira tradicional"""
    return re.match(padrao_placa, placa) is not None

# Exemplos de teste
placas = [
    "ABC-1234",   # válido
    "XYZ-0001",   # válido
    "abc-1234",   # inválido (minúsculas)
    "AB-1234",    # inválido (só 2 letras)
    "ABCD-1234",  # inválido (4 letras)
    "ABC1234",    # inválido (sem hífen)
]

print("=== Validação de Placas ===\n")
for placa in placas:
    print(f"{placa:10} → {'✅ válido' if validar_placa(placa) else '❌ inválido'}")
