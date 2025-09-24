'''
6. AFD – número par de 'a' Implemente um AFD que reconhece cadeias com número par de letras 'a'.
'''

def afd_par_de_a(cadeia: str) -> bool:
    """
    AFD que reconhece cadeias com número par de 'a'.
    Estado inicial: q0
    Estado de aceitação: q0 (número par de 'a')
    """
    estado = 'q0'  # estado inicial

    for simbolo in cadeia:
        if estado == 'q0':
            if simbolo == 'a':
                estado = 'q1'
            elif simbolo == 'b':
                estado = 'q0'  # permanece
            else:
                return False  # símbolo inválido
        elif estado == 'q1':
            if simbolo == 'a':
                estado = 'q0'
            elif simbolo == 'b':
                estado = 'q1'  # permanece
            else:
                return False  # símbolo inválido

    # aceita se terminar no estado q0
    return estado == 'q0'


# Testes
testes = ["", "a", "aa", "ababa", "baba", "aaa", "bbbb"]

print("=== AFD: Número Par de 'a' ===")
for teste in testes:
    resultado = afd_par_de_a(teste)
    print(f"{teste:10} → {'Aceita ✅' if resultado else 'Rejeita ❌'}")
