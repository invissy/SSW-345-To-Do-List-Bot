import discord
import responses
import config

# Send messages
async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        # await message.author.send(response) if is_private else await message.channel.send(response)
        await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = config.TOKEN
    client = discord.Client(intents=discord.Intents.all())
    # intents: https://discord.com/developers/docs/topics/gateway#list-of-intents

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

        # If the user message contains a '?' in front of the text, it becomes a private message
        # if user_message[0] == '?':
        #     user_message = user_message[1:]  # [1:] Removes the '?'
        #     await send_message(message, user_message, is_private=True)
        # else:
        #     await send_message(message, user_message, is_private=False)

        await send_message(message, user_message, is_private=False)
    # Remember to run your bot with your personal TOKEN
    client.run(TOKEN)