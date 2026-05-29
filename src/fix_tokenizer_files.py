from transformers import AutoTokenizer
from pathlib import Path

modelo_base = "pierreguillou/gpt2-small-portuguese"
modelo_path = Path("models/bookcraft-model")

print("Carregando tokenizer base...")
tokenizer = AutoTokenizer.from_pretrained(modelo_base)

print("Salvando arquivos completos do tokenizer no modelo final...")
tokenizer.save_pretrained(modelo_path)

print("Arquivos do tokenizer salvos com sucesso!")
print(f"Pasta: {modelo_path}")