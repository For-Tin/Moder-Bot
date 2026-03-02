import disnake
from disnake.ext import commands
import os
from dotenv import load_dotenv

class Client(commands.Bot):

    async def on_ready(self):

        await self.change_presence(status=disnake.Status.dnd)

        print("""
                ██████╗  ██████╗ ██████╗ 
                ██╔══██╗██╔═══██╗██╔══██╗
                ██████╔╝██║   ██║██████╔╝
                ██╔══██╗██║   ██║██╔══██╗
                ██████╔╝╚██████╔╝██████╔╝
                ╚═════╝  ╚═════╝ ╚═════╝ 
            """)

if __name__ == "__main__":

    client = Client(command_prefix="bob!", intents=disnake.Intents.all())

    client.load_extension("cogs.commands.kick")
    client.load_extension("cogs.commands.ban")
    client.load_extension("cogs.logs.message_logs")
    client.load_extension("cogs.logs.reaction_logs")

    load_dotenv()

    client.run(os.getenv("TOKEN_BOT"))
