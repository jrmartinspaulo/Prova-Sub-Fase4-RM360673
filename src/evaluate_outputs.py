from transformers import AutoTokenizer, AutoModelForCausalLM
from pathlib import Path

modelo_path = "models/bookcraft-model"

print("Carregando modelo treinado...")

tokenizer = AutoTokenizer.from_pretrained(modelo_path)
model = AutoModelForCausalLM.from_pretrained(modelo_path)

prompts = [
    "Gênero: Fantasia | Tom: Épico | Público: Jovens adultos | Sinopse:",
    "Gênero: Ficção Científica | Tom: Futurista | Público: Adultos | Sinopse:",
    "Gênero: Suspense | Tom: Tenso | Público: Adultos | Sinopse:",
    "Gênero: Romance | Tom: Emocional | Público: Jovens adultos | Sinopse:",
    "Gênero: Terror | Tom: Misterioso | Público: Adultos | Sinopse:"
]

parametros = [
    {
        "nome": "Criativo",
        "temperature": 1.0,
        "top_k": 50,
        "top_p": 0.95
    },
    {
        "nome": "Equilibrado",
        "temperature": 0.8,
        "top_k": 40,
        "top_p": 0.9
    },
    {
        "nome": "Conservador",
        "temperature": 0.6,
        "top_k": 30,
        "top_p": 0.85
    }
]

resultados = []

for prompt in prompts:
    for config in parametros:
        inputs = tokenizer(prompt, return_tensors="pt")

        output = model.generate(
            **inputs,
            max_length=110,
            temperature=config["temperature"],
            top_k=config["top_k"],
            top_p=config["top_p"],
            repetition_penalty=1.3,
            no_repeat_ngram_size=3,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )

        texto_gerado = tokenizer.decode(
            output[0],
            skip_special_tokens=True
        )

        resultados.append(
            f"## Prompt\n{prompt}\n\n"
            f"### Configuração: {config['nome']}\n"
            f"- temperature: {config['temperature']}\n"
            f"- top_k: {config['top_k']}\n"
            f"- top_p: {config['top_p']}\n\n"
            f"### Texto gerado\n{texto_gerado}\n\n"
            "---\n"
        )

output_path = Path("docs/exemplos_gerados.md")
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text("\n".join(resultados), encoding="utf-8")

print("Avaliação gerada com sucesso!")
print(f"Arquivo salvo em: {output_path}")