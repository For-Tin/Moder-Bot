import disnake
from disnake.ext import commands

import supabase

from utils import colors

class BalanceCommand(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="balance", description="Check your balance")
    async def balance(self, inter: disnake.ApplicationCommandInteraction):

        db: supabase.Client = self.bot.db
        response = db.table("users").select('username, balance').eq("username", inter.user.name).maybe_single().execute()

        if response == None:
            response = db.table("users").insert({"username":inter.user.name}).execute()
            response.data = response.data[0]
            
        embed = disnake.Embed(color=colors.GREEN, title="Your balance:", description=f"{response.data['balance']}")
        
        await inter.response.send_message(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(BalanceCommand(bot))
