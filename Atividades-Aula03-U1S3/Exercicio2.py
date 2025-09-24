"""2. Analisadores Léxicos em Compiladores

Exemplo: Tokenização de um Código-Fonte

Compiladores utilizam Autômatos Finitos Determinísticos (AFD) para transformar um programa em tokens.

Entrada:

int x = 10;

Tokens gerados:

Token

Tipo

int

Palavra-chave

x

Identificador

=

Operador

10

Número

;

Delimitador

Essa técnica é usada para entender e interpretar linguagens de programação."""

import re

# Definição de padrões para os tokens
token_specification = [
    ("PALAVRA_CHAVE", r"\b(int|float|if|else|while|for|return)\b"),
    ("IDENTIFICADOR", r"[a-zA-Z_][a-zA-Z0-9_]*"),
    ("NUMERO", r"\b\d+\b"),
    ("OPERADOR", r"[=+\-*/<>]"),
    ("DELIMITADOR", r"[;{}()]"),
    ("ESPACO", r"[ \t\n]+"),  # Ignorar espaços e quebras de linha
    ("DESCONHECIDO", r".")    # Qualquer coisa não reconhecida
]

# Combinar todos os padrões em uma regex única
token_regex = "|".join(f"(?P<{nome}>{regex})" for nome, regex in token_specification)

def analisar_codigo(codigo: str):
    tokens = []
    for match in re.finditer(token_regex, codigo):
        tipo = match.lastgroup
        valor = match.group()
        if tipo == "ESPACO":  # Ignorar espaços
            continue
        tokens.append((valor, tipo))
    return tokens


# Exemplo de uso
codigo_fonte = "int x = 10;"

print("=== Código de Entrada ===")
print(codigo_fonte, "\n")

print("=== Tokens Gerados ===")
tokens = analisar_codigo(codigo_fonte)
print(f"{'Token':15} Tipo")
print("-" * 30)
for valor, tipo in tokens:
    print(f"{valor:15} {tipo}")
