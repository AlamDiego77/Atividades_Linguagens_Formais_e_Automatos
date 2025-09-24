"""1. Validação de Formatos com Expressões Regulares

Exemplo: Validação de Endereço de E-mail

Expressões regulares são amplamente usadas para validar padrões em strings. Um validador de e-mail pode usar a seguinte expressão regular:

^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$

Aplicado em formulários de cadastros, evita entradas inválidas e melhora a qualidade dos dados armazenados.

"""

import re

# Expressão regular para validar e-mails
regex_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def validar_email(email: str) -> bool:
    """Valida um endereço de e-mail utilizando expressão regular"""
    return re.match(regex_email, email) is not None


print("=== Validador de E-mails ===")
print("Digite um e-mail para testar (ou 'sair' para encerrar)")

while True:
    email = input("E-mail: ").strip()
    
    if email.lower() == "sair":
        print("Encerrando o programa...")
        break
    
    if validar_email(email):
        print("✅ E-mail VÁLIDO!\n")
    else:
        print("❌ E-mail INVÁLIDO!\n")

