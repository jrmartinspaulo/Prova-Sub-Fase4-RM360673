import pandas as pd
import re

DATASET_PATH = "data/sinopses_dataset.csv"

df = pd.read_csv(DATASET_PATH)

print("VALIDAÇÃO DO DATASET")
print("=" * 50)

print(f"Total de registros: {len(df)}")
print(f"Colunas: {list(df.columns)}")
print(f"Valores nulos: {df.isnull().sum().sum()}")
print(f"Duplicados: {df.duplicated().sum()}")

print("\nDistribuição por gênero:")
generos = df["texto"].str.extract(r"Gênero: (.*?) \|")[0]
print(generos.value_counts().sort_index())

print("\nDistribuição por subgênero:")
subgeneros = df["texto"].str.extract(r"Subgênero: (.*?) \|")[0]
print(subgeneros.value_counts().sort_index())

print("\nTamanho médio dos textos:")
df["qtd_caracteres"] = df["texto"].str.len()
df["qtd_palavras"] = df["texto"].str.split().str.len()

print(f"Média de caracteres: {df['qtd_caracteres'].mean():.2f}")
print(f"Mínimo de caracteres: {df['qtd_caracteres'].min()}")
print(f"Máximo de caracteres: {df['qtd_caracteres'].max()}")

print(f"Média de palavras: {df['qtd_palavras'].mean():.2f}")
print(f"Mínimo de palavras: {df['qtd_palavras'].min()}")
print(f"Máximo de palavras: {df['qtd_palavras'].max()}")

print("\nChecando formato esperado:")
padrao = r"^Gênero: .+ \| Subgênero: .+ \| Tom: .+ \| Público: .+ \| Sinopse: .+"
formato_ok = df["texto"].apply(lambda x: bool(re.match(padrao, str(x))))
print(f"Registros com formato correto: {formato_ok.sum()} de {len(df)}")

print("\nPossíveis problemas gramaticais conhecidos:")
problemas = [
    "medo de coragem",
    "espadas encantada",
    "memórias apagado",
    "livros proibido ",
    "cartões de cidadania apagado"
]

for problema in problemas:
    qtd = df["texto"].str.contains(problema, case=False, regex=False).sum()
    print(f"{problema}: {qtd}")

print("\nValidação de balanceamento por gênero:")
balanceamento_esperado = 112
for genero, qtd in generos.value_counts().sort_index().items():
    status = "OK" if qtd == balanceamento_esperado else "ATENÇÃO"
    print(f"{genero}: {qtd} registros - {status}")

print("\nValidação de campos obrigatórios:")
campos_obrigatorios = ["Gênero:", "Subgênero:", "Tom:", "Público:", "Sinopse:"]
for campo in campos_obrigatorios:
    qtd = df["texto"].str.contains(campo, regex=False).sum()
    status = "OK" if qtd == len(df) else "ATENÇÃO"
    print(f"{campo} presente em {qtd} registros - {status}")

print("\nExemplos aleatórios:")
print(df.sample(10, random_state=42)["texto"].to_string(index=False))

print("\nValidação concluída.")