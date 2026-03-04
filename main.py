import disnake
from disnake.ext import commands

import os
from dotenv import load_dotenv

import supabase
from supabase import create_client

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

    bot = Client(command_prefix="bob!", intents=disnake.Intents.all())

    bot.load_extension("cogs.commands.help")
    bot.load_extension("cogs.commands.mod.kick")
    bot.load_extension("cogs.commands.mod.ban")
    bot.load_extension("cogs.commands.bank.balance")
    bot.load_extension("cogs.logs.message_logs")
    bot.load_extension("cogs.logs.reaction_logs")

    load_dotenv()

    url: str = os.getenv("SUPABASE_URL")
    key: str = os.getenv("SUPABASE_KEY")
    db_client: supabase.Client = create_client(url, key)
    bot.db = db_client

    bot.run(os.getenv("TOKEN_BOT"))
