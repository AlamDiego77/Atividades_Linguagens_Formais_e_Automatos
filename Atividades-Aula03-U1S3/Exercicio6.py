'''6. Segurança da Informação e Firewalls

Exemplo: Detecção de Ataques SQL Injection

Firewalls utilizam Autômatos Finitos para identificar padrões maliciosos em entradas de dados.

Entrada maliciosa:

' OR '1'='1' --

Se detectado por um firewall, a conexão é bloqueada, prevenindo invasões.

'''

import re

# Padrões comuns de SQL Injection
padroes_sql_injection = [
    r"('.+--)",         # Ex: ' OR '1'='1' --
    r"(\bOR\b.+=.+)",   # Ex: OR 1=1
    r"(\bUNION\b.+\bSELECT\b)", # UNION SELECT
    r"(\bDROP\b.+\bTABLE\b)",   # DROP TABLE
    r"(\bINSERT\b.+\bINTO\b)",  # INSERT INTO
    r"(\bUPDATE\b.+\bSET\b)",   # UPDATE ... SET
]

# Combina todos os padrões
regex_sql = re.compile("|".join(padroes_sql_injection), re.IGNORECASE)

def detectar_sql_injection(entrada: str) -> bool:
    """Detecta se a entrada contém padrões de SQL Injection"""
    return bool(regex_sql.search(entrada))


# Exemplos de uso
entradas = [
    "admin' OR '1'='1' --",
    "SELECT * FROM users WHERE id=1",
    "DROP TABLE usuarios;",
    "normalUser",
    "teste UNION SELECT senha FROM contas"
]

print("=== Teste de Detecção de SQL Injection ===\n")
for entrada in entradas:
    if detectar_sql_injection(entrada):
        print(f"🚨 Entrada suspeita detectada: {entrada}")
    else:
        print(f"✅ Entrada segura: {entrada}")
