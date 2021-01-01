import discord

client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send('MESSAGE HERE')
      print(f"Messaged {user.name}")
    except:
       print(f"Could not message {user.name}")

client.run('TOKEN HERE', bot=False)

