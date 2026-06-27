# Seção para rodar o script na main sem ter que ficar movendo arquivos:

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
""" import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) """
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

import os
from random import randint
from dotenv import load_dotenv
from Sistemas.gerarNpc import gerarNome
from huggingface_hub import InferenceClient

load_dotenv()

HF_TOKEN = os.getenv('HF_TOKEN') # Esta linha copia a variável de ambiente de mesmo nome que deve ser inclusa no arquivo .env, conforme indicado pelo .env.example

client = InferenceClient(token=HF_TOKEN)

# Função para gerar a história do personagem:

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def gerar_backstory(nome, idade):
    system_prompt = (
        "Você é um escritor especialista em bibliografias, que escreve textos simplistas e concisos. "
        "Sua tarefa é criar um resumo da pessoa citada (background), sendo imersivo e criativo sobre seu dia a dia (contexto: a pessoa se encontra em uma estação de trem). "
        "Sempre seguindo estritamente estas regras:"
        "1. A história deve ter EXATAMENTE 4 frases completas.\n"
        "2. Escreva o suficiente para que 200 tokens comporte a resposta completa, sem cortes.\n"
        "3. Responda SEMPRE em português.\n"
        "4. Utilize a seguinte estrutura na resposta: **Background:** Nome Sobrenome, de xx anos,... (Quem é a pessoa e o que faz da vida)\n"
    )
    
    user_prompt = f"Gere uma história para o personagem: Nome: {nome}, Idade: {idade} anos."
    
    mensagens = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
    try:
        resposta = client.chat_completion(
            model=os.getenv('MODEL'),
            messages=mensagens,
            max_tokens=200,
            temperature=0.8
        )
        return resposta.choices[0].message.content
    except Exception as e:
        return f"Erro ao gerar história: {e}"

#botar pronome neutro? -> pensar sobre tratativas de gênero/sexualidade
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Conversando com o personagem criado:

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def conversar_com_personagem(nome, idade, backstory, pergunta_jogador):
    system_prompt = (
        f"Você é um personagem chamado {nome}, de {idade} anos. "
        f"Esta é a sua história de fundo:\n{backstory}\n\n"
        "Sua tarefa é responder à pergunta do jogador (que é o maquinista responsável) incorporando este personagem de forma realista e imersiva, mas seguindo estritamente estas regras:"
        "1. Escreva SEMPRE em terceira pessoa (narre as ações e reações do personagem).\n"
        "2. A resposta deve ter EXATAMENTE 3 frases completas.\n"
        "3. Das 3 frases completas, sempre traga uma frase que cite diretamente palavras do personagem entre áspas.\n"
        "4. Responda SEMPRE em português.\n"
        "5. NÃO copie exemplos. Crie uma reação original baseada no contexto da pergunta."
    )

    try:
        resposta = client.chat_completion(
            model="Qwen/Qwen2.5-7B-Instruct",
            messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": pergunta_jogador}],
            max_tokens=100,
            temperature=0.9
        )
        return resposta.choices[0].message.content
    except Exception as e:
        return f"Erro na resposta do personagem: {e}"
    
# Testando os scripts:

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
""" nome_personagem = gerarNome()
idade_aleatoria = randint(18, 60)

#print(f"Gerando história para {nome_personagem}, {idade_aleatoria} anos...\n")
historia_final = gerar_backstory(nome_personagem, idade_aleatoria)

print(historia_final)

pergunta = input(f'\nMaquinista, deseja fazer alguma pergunta para {nome_personagem.split(" ")[0]}?\n')
if pergunta.capitalize() in ['Não', 'Negativo']:
    print(f'\n{nome_personagem.split(" ")[0]} vai embora.')
else:
    print(f'\n{conversar_com_personagem(nome_personagem, idade_aleatoria, historia_final, pergunta)}') """
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////