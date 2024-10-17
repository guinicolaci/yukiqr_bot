import discord
import qrcode
from io import BytesIO
import requests
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém o token do bot do Discord a partir das variáveis de ambiente
TOKEN = os.getenv('DISCORD_TOKEN')

# Configura as intenções do bot para receber o conteúdo das mensagens
intents = discord.Intents.default()
intents.message_content = True

# Inicializa o cliente do Discord com as intenções configuradas
client = discord.Client(intents=intents)

# Evento acionado quando o bot está pronto
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')  # Exibe uma mensagem indicando que o bot está logado

# Evento acionado quando uma mensagem é enviada em um canal
@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Ignora mensagens enviadas pelo próprio bot

    if client.user in message.mentions:
        # Verifica se a mensagem mencionada é uma resposta a outra mensagem
        referenced_message = message.reference.resolved if message.reference else None

        if referenced_message:
            # Transforma a mensagem referenciada em QR code
            text_to_convert = referenced_message.content
        else:
            # Transforma o texto da própria mensagem em QR code
            text_to_convert = message.content.replace(f'<@{client.user.id}>', '').strip()

        if not text_to_convert:
            await message.channel.send("Por favor, forneça o texto ou URL para converter em QR code.")
            return  # Se o texto estiver vazio, pede ao usuário que forneça um texto ou URL

        # Gera o QR code com o texto fornecido
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text_to_convert)
        qr.make(fit=True)

        # Converte a imagem do QR code em bytes
        img = qr.make_image(fill_color="black", back_color="white")

        with BytesIO() as image_binary:
            img.save(image_binary, 'PNG')  # Salva a imagem em formato PNG
            image_binary.seek(0)
            # Envia a imagem do QR code no canal
            await message.channel.send(file=discord.File(fp=image_binary, filename='qrcode.png'))

# Inicia o bot com o token fornecido
client.run(TOKEN)