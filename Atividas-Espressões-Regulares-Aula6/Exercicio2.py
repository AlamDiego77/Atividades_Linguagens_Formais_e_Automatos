'''2. Identificação de e-mails válidos Utilize regex para validar se uma string é um endereço de e-mail básico (ex: nome@dominio.com). Resposta: import re # Regex para e-mails básicos padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'''

import re

# Regex para e-mails básicos
padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'

def validar_email(email: str) -> bool:
    """Valida se uma string é um e-mail básico"""
    return re.match(padrao_email, email) is not None


# Exemplos de teste
emails = [
    "usuario@dominio.com",       # válido
    "meu.email@provedor.org",    # válido
    "nome.sobrenome@empresa.co", # válido
    "usuario@dominio",           # inválido (sem TLD)
    "usuario#dominio.com",       # inválido (sem @)
    "@dominio.com",              # inválido
]

print("=== Validação de E-mails ===\n")
for email in emails:
    print(f"{email:30} → {'✅ válido' if validar_email(email) else '❌ inválido'}")
