import random
import numpy as np
import pandas as pd
import torch

from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling
)

SEED = 42

random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)

print("Carregando dataset...")

df = pd.read_csv("data/sinopses_dataset.csv")
df = df.dropna()
df = df.drop_duplicates()

print(f"Total de registros após limpeza: {len(df)}")

dataset = Dataset.from_pandas(df)

# MODELO EM PORTUGUÊS
modelo_base = "pierreguillou/gpt2-small-portuguese"

print("Carregando modelo e tokenizer em português...")

tokenizer = AutoTokenizer.from_pretrained(modelo_base)
model = AutoModelForCausalLM.from_pretrained(modelo_base)

tokenizer.pad_token = tokenizer.eos_token
model.config.pad_token_id = tokenizer.eos_token_id

def tokenize_function(examples):
    return tokenizer(
        examples["texto"],
        truncation=True,
        padding="max_length",
        max_length=192
    )

print("Tokenizando dataset...")

tokenized_dataset = dataset.map(
    tokenize_function,
    batched=True,
    remove_columns=["texto"]
)

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False
)

training_args = TrainingArguments(
    output_dir="models/bookcraft-model",
    num_train_epochs=10,
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    learning_rate=2e-5,
    weight_decay=0.01,
    warmup_steps=75,
    save_strategy="epoch",
    save_total_limit=2,
    logging_steps=20,
    report_to=[],
    seed=SEED
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    data_collator=data_collator
)

print("Iniciando treinamento em português...")

trainer.train()

trainer.save_model("models/bookcraft-model")
tokenizer.save_pretrained("models/bookcraft-model")

print("Modelo treinado e salvo com sucesso!")
