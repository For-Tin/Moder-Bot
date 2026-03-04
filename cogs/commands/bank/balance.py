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
        response = db.table("users").select('discord_id, balance').eq("discord_id", inter.user.id).maybe_single().execute()

        if response is None:
            response = db.table("users").insert({"discord_id":inter.user.id, "name":inter.user.display_name, "username":inter.user.name}).execute()
            response.data = response.data[0]

        embed = disnake.Embed(color=colors.YELLOW,
                              title="Your Card:",
                              description=f"Balance: {response.data["balance"]}**₿**")
        
        embed.set_thumbnail(inter.user.display_avatar.url)
        
        await inter.response.send_message(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(BalanceCommand(bot))
