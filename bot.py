import discord
import responses
from time import sleep

async def send_message(message, user_message,  is_private):
    try:
        if(str(message.author) == 'rukeee'):
            response = responses.frankResponses(user_message)
        else: 
            response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except:
        print(Exception)

def run_discord_bot():
    TOKEN = 'MTE3NTA4Nzg0NDM4MTk1NDExOA.GOUQ-A.Byb3HlCBjeUnqyY22-LRAx5U8qFdk77iFc9CUU'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents = intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        await client.get_channel(1175157852340506685).send("I am alive")
        sleep(1)
        await client.get_channel(1175157852340506685).send("Hello, world!")


    @client.event
    async def on_message(message):
        channel = str(message.channel)
        if message.author == client.user or channel != "just-entropy":
            return
        
        username = str(message.author)
        user_message = str(message.content)
        print(f'{username} said {user_message} in the {channel} channel')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message.lower(), is_private = True)
        else:
            await send_message(message, user_message.lower(), is_private = False)

    client.run(TOKEN)