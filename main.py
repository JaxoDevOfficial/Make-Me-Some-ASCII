import discord, os, time

client = discord.Client()
id = 0 # Put your user ID here!

open("help.ascii", "w").write('''**Make Me Some ASCII**
*Version 1.0*

__Written by:__
> another
__With help from:__
> T3Manager''')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author.id == id:
    if message.content.lower().startswith('mms-ascii'):
      name = message.content.split(" ")[1]
      try:
        open(name+".ascii")
      except:
        msg = await message.reply(content=f"**ASCII \"{name}\" does not exist!**")
        time.sleep(2)
        await msg.delete()
        await message.delete()
      await message.reply(open(name+".ascii", "r").read())
      
client.run(os.environ['token'], bot=False)

# HOW TO SETUP!
# Replace the ID in "id" with your Discord ID.
# Add your token as a secret named token.
# Run "pip install discord" in the shell.
# And your done!