from transformers import AutoTokenizer, AutoModelForCausalLM

modelo_path = "models/bookcraft-model"

print("Carregando modelo treinado...")

tokenizer = AutoTokenizer.from_pretrained(modelo_path)
model = AutoModelForCausalLM.from_pretrained(modelo_path)

prompt = (
    "Gênero: Fantasia | "
    "Subgênero: alta fantasia | "
    "Tom: Épico | "
    "Público: Jovens adultos | "
    "Sinopse:"
)

inputs = tokenizer(prompt, return_tensors="pt")

output = model.generate(
    **inputs,
    max_new_tokens=100,
    temperature=0.8,
    top_k=45,
    top_p=0.9,
    repetition_penalty=1.3,
    no_repeat_ngram_size=3,
    do_sample=True,
    pad_token_id=tokenizer.eos_token_id
)

texto_gerado = tokenizer.decode(
    output[0],
    skip_special_tokens=True
)

def limitar_frases(texto, limite=4):
    partes = texto.split(".")
    frases = []

    for parte in partes:
        parte = parte.strip()
        if parte:
            frases.append(parte + ".")

    if len(frases) > limite:
        texto = " ".join(frases[:limite])
    else:
        texto = " ".join(frases)

    return texto.strip()

texto_gerado = limitar_frases(texto_gerado, limite=4)

print("\n===== TEXTO GERADO =====\n")
print(texto_gerado)