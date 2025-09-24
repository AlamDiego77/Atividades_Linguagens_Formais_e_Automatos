'''5. Análise de DNA e Bioinformática

Exemplo: Identificação de Sequências de DNA

A biologia computacional usa Expressões Regulares para identificar padrões genéticos.

ER para detectar um gene codificante:

ATG([ATCG]{3})+(TAA|TAG|TGA)

Isso ajuda na pesquisa de genes e doenças hereditárias.'''

import re

# Expressão regular para identificar genes codificantes
regex_gene = r"ATG(?:[ATCG]{3})+(?:TAA|TAG|TGA)"

def encontrar_genes(sequencia: str):
    """Retorna todos os genes encontrados na sequência de DNA"""
    return re.findall(regex_gene, sequencia)


# Exemplo de uso
sequencia_dna = "AAATGCGTACGTAAAGCTAGATGTTTCCCTGA"

print("=== Sequência de DNA ===")
print(sequencia_dna, "\n")

genes = encontrar_genes(sequencia_dna)

print("=== Genes Encontrados ===")
if genes:
    for g in genes:
        print("🔹", g)
else:
    print("❌ Nenhum gene encontrado")
