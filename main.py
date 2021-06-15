import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if(message.author!=self.user):
            await message.channel.send('Message from {0.author}: {0.content}'.format(message))


client = MyClient()
"""VC = discord.VoiceClient(client,"General")
await VC.connect(reconnect=True,timeout=60);"""
client.run('ODU0MzAxMTA1Mjc4Mjg3ODky.YMh75w.ZrFwWXDW5l-1AzK-NvbNjKNbcDw')