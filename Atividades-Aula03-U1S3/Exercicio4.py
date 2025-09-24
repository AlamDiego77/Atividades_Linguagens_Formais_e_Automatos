'''4. Protocolos de Redes e Verificação de Estados

Exemplo: TCP 3-Way Handshake

O protocolo TCP utiliza Autômatos Finitos para gerenciar conexões.

Estados do protocolo:

LISTEN → O servidor aguarda conexões.
SYN_SENT → O cliente envia um pacote SYN.
SYN_RECEIVED → O servidor responde com SYN-ACK.
ESTABLISHED → O cliente responde com ACK e a conexão é estabelecida.
Isso garante comunicação confiável entre dispositivos.'''

# Definição dos estados do TCP
ESTADOS = ["LISTEN", "SYN_SENT", "SYN_RECEIVED", "ESTABLISHED"]

# Transições (simulação do AFD)
transicoes = {
    "LISTEN": "SYN_SENT",         # Cliente envia SYN
    "SYN_SENT": "SYN_RECEIVED",   # Servidor responde SYN-ACK
    "SYN_RECEIVED": "ESTABLISHED" # Cliente envia ACK
}

def tcp_handshake():
    estado = "LISTEN"
    print(f"🔵 Estado inicial: {estado}")

    while estado in transicoes:
        proximo = transicoes[estado]
        print(f"➡️ Transição: {estado} → {proximo}")
        estado = proximo

    print(f"✅ Conexão estabelecida no estado: {estado}")


# Execução do autômato
if __name__ == "__main__":
    print("=== Simulação do TCP 3-Way Handshake ===\n")
    tcp_handshake()
