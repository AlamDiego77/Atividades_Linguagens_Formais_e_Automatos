'''3. Assistentes Virtuais e Linguagem Natural

Exemplo: Chatbots e Comandos de Voz

Chatbots utilizam Gramáticas Livres de Contexto (GLC) para interpretar comandos.

Gramática Simples:

S → Comando Objeto

Comando → "ligue" | "desligue" | "abra"

Objeto → "luz" | "portão" | "música"

Exemplo de Entrada: "ligue a luz"

Saída Esperada: O assistente ativa o interruptor.'''

# Definição da gramática simples
comandos = ["ligue", "desligue", "abra"]
objetos = ["luz", "portão", "música"]

def interpretar_comando(frase: str) -> str:
    palavras = frase.lower().split()

    # Estrutura esperada: Comando + objeto (ex: "ligue luz")
    if len(palavras) < 2:
        return "❌ Comando incompleto."

    comando = palavras[0]
    objeto = palavras[-1]

    if comando not in comandos:
        return f"❌ Comando desconhecido: {comando}"

    if objeto not in objetos:
        return f"❌ Objeto desconhecido: {objeto}"

    # Saída simulada (ação do assistente)
    if comando == "ligue":
        return f"✅ Assistente: ligando a {objeto}..."
    elif comando == "desligue":
        return f"✅ Assistente: desligando a {objeto}..."
    elif comando == "abra":
        return f"✅ Assistente: abrindo {objeto}..."
    else:
        return "❌ Não entendi o comando."

# Exemplos de uso
entradas = [
    "ligue luz",
    "desligue música",
    "abra portão",
    "ligue televisão"  # objeto inválido
]

print("=== Testes da Gramática ===\n")
for frase in entradas:
    print(f"Entrada: {frase}")
    print(interpretar_comando(frase))
    print()
