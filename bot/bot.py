# libraries https://discord.com/developers/docs/topics/community-resources
import discord #https://discordpy.readthedocs.io/en/latest/
# https://discordpy.readthedocs.io/en/stable/ext/commands/index.html
import config
import responses
import taskBoard

# Send messages
async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        # await message.author.send(response) if is_private else await message.channel.send(response)
        await message.channel.send(response)

    except Exception as e:
        print(e)


# async def new_thread(threadName):
    # await create_thread(threadName)

def run_discord_bot():
    client = discord.Client(intents=discord.Intents.all()) # intents: https://discord.com/developers/docs/topics/gateway#list-of-intents

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user: # Bot only reacts to other users messages
            return

        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")

        await send_message(message, user_message, is_private=False)
        
        if user_message == "thread":
            await taskBoard.new_thread("thread", message)
        if user_message == "private thread":
            await taskBoard.new_thread("private thread", client)

    client.run(config.TOKEN)