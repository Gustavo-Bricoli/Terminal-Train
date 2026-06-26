import os
from random import randint
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

# 1. Coloque aqui o seu token de leitura (Read) da Hugging Face
HF_TOKEN = os.getenv('HF_TOKEN') # Esta linha copia a variável de ambiente de mesmo nome que deve ser inclusa no arquivo .env, conforme indicado pelo .env.example

# 2. Inicializa o cliente passando o token explicitamente
client = InferenceClient(token=HF_TOKEN)

# Função para gerar a história do personagem
def gerar_backstory(nome, idade):
    system_prompt = (
        "Você é um escritor especialista bibliografias, que escreve textos simplistase concisos. "
        "Sua tarefa é criar histórias de fundo (backstories) curtas, imersivas e criativas sobre pessoas do dia a dia (que se podem encontrar em uma estação de trem). "
        "Responda SEMPRE em português e use a seguinte estrutura:\n"
        "**Descrição:** (Quem é a pessoa e o que faz da vida)\n"
    )
    
    user_prompt = f"Gere uma história para o personagem: Nome: {nome}, Idade: {idade} anos."
    
    mensagens = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
    try:
        resposta = client.chat_completion(
            model="Qwen/Qwen2.5-7B-Instruct",
            messages=mensagens,
            max_tokens=150,
            temperature=0.8
        )
        return resposta.choices[0].message.content
    except Exception as e:
        return f"Erro ao gerar história: {e}"

# --- TESTANDO O SCRIPT ---
nome_personagem = "Júlia Roberta"
idade_aleatoria = randint(18, 60)

print(f"Gerando história para {nome_personagem}, {idade_aleatoria} anos...\n")
historia_final = gerar_backstory(nome_personagem, idade_aleatoria)

print(historia_final)

# Botar pronome neutro?