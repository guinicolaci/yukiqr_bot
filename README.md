## YukiQR Bot
YukiQR é um bot do Discord que transforma qualquer mensagem em um QR code! Basta marcar o bot em uma mensagem ou mencionar o bot com a mensagem que deseja converter, e ele cuidará do resto.

# Funcionalidades

- Criação de QR Code a partir de mensagens: Transforme qualquer mensagem do Discord em um QR code simplesmente mencionando o YukiQR.

- Suporte para mensagens referenciadas: Responda a uma mensagem existente mencionando o YukiQR para convertê-la em um QR code.

# Como Usar
- Modo 1: Converter Mensagem Direta
Mencione o bot e escreva a mensagem que deseja converter em QR code: 
"@YukiQR Transforme isso em um QR code"

Modo 2: Converter Mensagem Referenciada
Responda a uma mensagem mencionando o bot para convertê-la em um QR code.
@YukiQR

## Instalação e Configuração
Pré-requisitos
Python 3.8 ou superior

Pip (gerenciador de pacotes do Python)

Conta do Discord e acesso ao Discord Developer Portal

Passos para Instalação
Clone o repositório:


git clone https://github.com/guinicolaci/yukiqr_bot.git
cd yukiqr

Instale as dependências:

pip install -r requirements.txt

# Configure o token do bot:
Crie um arquivo .env na raiz do projeto e adicione seu token do bot do Discord
DISCORD_TOKEN=seu_token_do_discord

# Execute o bot:

python yuki_bot.py

# Dependências
- discord.py
- qrcode
- python-dotenv
- requests