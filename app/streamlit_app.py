import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM

st.set_page_config(
    page_title="BookCraft AI",
    page_icon="📚",
    layout="centered"
)

modelo_path = "models/bookcraft-model"

subgeneros_por_genero = {
    "Romance": [
        "romance contemporâneo",
        "romance dramático",
        "romance de reencontro",
        "romance epistolar",
        "romance de amadurecimento",
        "romance de segunda chance"
    ],
    "Fantasia": [
        "alta fantasia",
        "fantasia sombria",
        "fantasia medieval",
        "fantasia mágica",
        "fantasia de aventura",
        "fantasia épica"
    ],
    "Ficção Científica": [
        "space opera",
        "cyberpunk",
        "IA e consciência",
        "exploração espacial"
    ],
    "Suspense": [
        "suspense psicológico",
        "suspense policial",
        "thriller jurídico",
        "conspiração"
    ],
    "Terror": [
        "terror psicológico",
        "terror sobrenatural",
        "horror gótico",
        "terror de isolamento"
    ],
    "Drama": [
        "drama familiar",
        "drama social",
        "drama psicológico",
        "drama de superação"
    ],
    "Aventura": [
        "aventura arqueológica",
        "aventura marítima",
        "caça ao tesouro",
        "jornada de sobrevivência"
    ],
    "Mistério": [
        "mistério clássico",
        "mistério histórico",
        "mistério familiar",
        "mistério investigativo"
    ],
    "Distopia": [
        "distopia política",
        "distopia tecnológica",
        "distopia social",
        "distopia de vigilância"
    ]
}


@st.cache_resource
def carregar_modelo():
    tokenizer = AutoTokenizer.from_pretrained(modelo_path)
    model = AutoModelForCausalLM.from_pretrained(modelo_path)
    return tokenizer, model


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


def limpar_texto(texto):
    correcoes = {
        "medo de coragem": "medo e coragem",
        "espadas encantada": "espadas encantadas",
        "memórias apagado": "memórias apagadas",
        "livros proibido": "livros proibidos",
        "transformations": "transformações"
    }

    for errado, certo in correcoes.items():
        texto = texto.replace(errado, certo)

    texto = texto.strip()
    texto = limitar_frases(texto, limite=4)

    return texto


tokenizer, model = carregar_modelo()

st.title("📚 BookCraft AI")
st.subheader("Gerador de Sinopses Literárias com IA Generativa")

st.markdown("""
Esta aplicação utiliza **Hugging Face Transformers** com um modelo **GPT-2 em português ajustado por fine-tuning** para gerar sinopses originais de livros.

O projeto foi desenvolvido como um playground generativo para testar diferentes combinações de gênero, subgênero, tom, público-alvo e parâmetros de geração.
""")

genero = st.selectbox(
    "Gênero",
    list(subgeneros_por_genero.keys())
)

subgenero = st.selectbox(
    "Subgênero",
    subgeneros_por_genero[genero]
)

tom = st.selectbox(
    "Tom",
    [
        "Épico",
        "Sombrio",
        "Emocional",
        "Tenso",
        "Assustador",
        "Misterioso",
        "Inspirador",
        "Futurista",
        "Leve",
        "Reflexivo"
    ]
)

publico = st.selectbox(
    "Público",
    [
        "Jovens adultos",
        "Adultos",
        "Jovens",
        "Leitores iniciantes",
        "Leitores de fantasia",
        "Leitores de suspense"
    ]
)

st.markdown("### Ajustes do modelo")

temperature = st.slider(
    "Temperature",
    min_value=0.3,
    max_value=1.2,
    value=0.7,
    step=0.1
)

top_k = st.slider(
    "Top-K",
    min_value=10,
    max_value=100,
    value=35,
    step=5
)

top_p = st.slider(
    "Top-P",
    min_value=0.5,
    max_value=1.0,
    value=0.85,
    step=0.05
)

max_new_tokens = st.slider(
    "Quantidade máxima de novos tokens",
    min_value=50,
    max_value=140,
    value=100,
    step=10
)

limite_frases = st.slider(
    "Quantidade máxima de frases",
    min_value=2,
    max_value=6,
    value=4,
    step=1
)

if st.button("✨ Gerar Sinopse"):

    with st.spinner("Gerando sinopse... aguarde alguns segundos."):
        prompt = (
            f"Gênero: {genero} | "
            f"Subgênero: {subgenero} | "
            f"Tom: {tom} | "
            f"Público: {publico} | "
            f"Sinopse:"
        )

        inputs = tokenizer(prompt, return_tensors="pt")

        output = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            repetition_penalty=1.3,
            no_repeat_ngram_size=3,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )

        texto_gerado = tokenizer.decode(
            output[0],
            skip_special_tokens=True
        )

        texto_gerado = limpar_texto(texto_gerado)
        texto_gerado = limitar_frases(texto_gerado, limite=limite_frases)

    st.markdown("## 📖 Sinopse Gerada")
    st.success(texto_gerado)

st.markdown("---")

st.markdown("""
### Sobre o modelo

O modelo utilizado foi o **GPT-2 Small em português**, disponível na Hugging Face.

Para este projeto, foi realizado um processo de **fine-tuning** com um dataset próprio contendo **1008 exemplos de sinopses literárias**, estruturadas por:

- gênero;
- subgênero;
- tom;
- público-alvo;
- personagens;
- cenários;
- conflitos;
- elementos narrativos.

A aplicação permite testar o poder generativo do modelo por meio de controles interativos como **temperature**, **top-k**, **top-p**, quantidade máxima de tokens e limite de frases.

Durante o desenvolvimento, a qualidade das gerações foi avaliada e os parâmetros foram ajustados para melhorar coerência, originalidade e controle do texto gerado.
""")

st.caption("Projeto acadêmico - Machine Learning Engineering | Hugging Face Transformers + Streamlit")