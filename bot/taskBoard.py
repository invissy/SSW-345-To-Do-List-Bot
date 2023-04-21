async def new_thread(threadName, message):
    thread = await message.create_thread(name = threadName)
    await thread.send("hello :)")


# private thread
async def new_thread(threadName, client):
    channel = client.get_channel(int(1096277622708777050))
    thread = await channel.create_thread(name = threadName)
    await thread.send("hello :)")