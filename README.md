# 📚 BookCraft AI – Gerador de Sinopses Literárias com IA Generativa

## 📌 Sobre o Projeto

O **BookCraft AI** é um modelo generativo desenvolvido utilizando a biblioteca **Hugging Face Transformers** com o objetivo de gerar **sinopses literárias originais e criativas**.

O projeto foi desenvolvido como atividade da disciplina **Machine Learning Engineering – Prova Substitutiva Fase 4** da FIAP.

A proposta consiste em construir uma aplicação em estilo **playground generativo**, permitindo ao usuário testar diferentes combinações narrativas e explorar o potencial criativo da inteligência artificial.

---

## 🎯 Tema do Modelo Generativo

O tema escolhido para o modelo foi:

**Geração de sinopses literárias para livros fictícios.**

A aplicação permite gerar histórias com diferentes:

* gêneros;
* subgêneros;
* tons narrativos;
* públicos-alvo;
* parâmetros de geração.

---

## 🤖 Modelo Pré-Treinado Utilizado

Foi utilizado o modelo:

**GPT-2 Small em Português**
(Hugging Face Transformers)

Modelo base:

```text
pierreguillou/gpt2-small-portuguese
```

O modelo foi escolhido por apresentar:

* suporte à língua portuguesa;
* arquitetura autoregressiva adequada para geração textual;
* boa relação entre qualidade e complexidade computacional;
* compatibilidade com fine-tuning em dataset próprio.

---

## 🧠 Fine-Tuning do Modelo

Foi realizado um processo de **fine-tuning supervisionado** utilizando um dataset próprio.

O treinamento utilizou:

* Hugging Face Transformers
* PyTorch
* AutoModelForCausalLM
* Trainer API

O objetivo do ajuste foi especializar o modelo na geração de sinopses literárias coerentes e criativas.

---

## 📊 Dataset Utilizado

Foi construído um dataset próprio contendo:

**1008 exemplos de sinopses literárias.**

Os registros foram estruturados contendo:

* Gênero
* Subgênero
* Tom narrativo
* Público-alvo
* Cenários
* Personagens
* Conflitos
* Elementos narrativos

O dataset foi validado para garantir:

* ausência de duplicados;
* balanceamento entre gêneros;
* coerência textual;
* padronização estrutural;
* qualidade linguística.

---

## 🧩 Gêneros e Subgêneros

O dataset contempla múltiplos estilos literários.

### Gêneros

* Romance
* Fantasia
* Ficção Científica
* Suspense
* Terror
* Drama
* Mistério
* Aventura
* Distopia

### Exemplos de Subgêneros

* Alta fantasia
* Romance contemporâneo
* Exploração espacial
* Cyberpunk
* Terror sobrenatural
* Thriller jurídico
* Mistério investigativo
* Distopia tecnológica

---

## ⚙️ Playground Generativo

A aplicação foi desenvolvida em **Streamlit**.

O usuário pode controlar:

* Temperature
* Top-K
* Top-P
* Quantidade máxima de tokens
* Quantidade máxima de frases

Esses controles permitem avaliar:

* criatividade;
* coerência;
* aderência temática;
* originalidade das gerações.

---

## 🏗️ Arquitetura da Solução

Fluxo do projeto:

```text
Dataset próprio
        ↓
Pré-processamento
        ↓
Fine-tuning GPT-2 Português
        ↓
Modelo treinado
        ↓
Streamlit Playground
        ↓
Geração de sinopses
```

---

## 📂 Estrutura do Projeto

```text
app/
 └── streamlit_app.py

data/
 └── sinopses_dataset.csv

docs/
 └── exemplos_gerados.md

models/
 └── bookcraft-model/

src/
 ├── create_dataset.py
 ├── train_model.py
 ├── generate_text.py
 ├── evaluate_outputs.py
 └── validate_dataset.py
```

---

## ▶️ Como Executar

### 1. Criar ambiente virtual

```bash
python -m venv .venv
```

### 2. Ativar ambiente

Windows:

```bash
.venv\Scripts\activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar aplicação

```bash
streamlit run app/streamlit_app.py
```

---

## 🧪 Exemplos de Geração

### Romance

> Uma fotógrafa sonhadora encontra cartas antigas e aprende que amar novamente exige coragem.

### Terror

> Em uma casa abandonada, um ritual antigo transforma medo em presença constante.

### Ficção Científica

> Um androide consciente precisa impedir uma falha tecnológica que ameaça milhares de vidas.

### Fantasia

> Uma escriba descobre uma coroa amaldiçoada e enfrenta o medo ancestral dos reinos.

---

## 📈 Avaliação do Modelo

As gerações foram avaliadas considerando:

* coerência;
* criatividade;
* originalidade;
* aderência ao gênero;
* fluidez narrativa.

Os testes demonstraram boa capacidade de especialização após o fine-tuning.

---

## 🛠️ Tecnologias Utilizadas

* Python
* Hugging Face Transformers
* PyTorch
* Streamlit
* Pandas
* Datasets

---

## 🎥 Entrega

A entrega contempla:

* repositório GitHub;
* deployment Streamlit;
* vídeo demonstrativo explicando a estratégia do modelo.

---

Projeto acadêmico – FIAP
Machine Learning Engineering – Prova Substitutiva Fase 4
