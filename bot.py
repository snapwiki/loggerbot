import discord
from mw_api_client import Wiki
from os import environ

wiki = Wiki("https://snapwiki.miraheze.org/w/api.php", "Snap! Wiki Technical Change Logger/1.0.0")
wiki.clientlogin("R4356thBot", environ.WIKI_PASSWORD)
print("Logged in to wiki.")

class Bot(discord.Client):
    async def on_ready(self):
        print("Logged in to Discord.")
    async def on_message(self, message):
        if message.content.startswith("!log"):
            content = message.content
            content = content.replace("!log ", "")
            page = wiki.page("Snap! Wiki:Technical Changelog")
            pagecontent = page.read()
            pagecontent += "\n" + "* ~~~~~ - " + content
            summ = "New change: " + content
            page.edit(pagecontent, summ)

client = Bot()
client.run(environ.DISCORD_TOKEN)
