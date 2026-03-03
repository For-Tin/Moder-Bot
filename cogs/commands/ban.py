import disnake
from disnake.ext import commands

from utils import colors

class BanCommand(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="ban", description="Ban member")
    @commands.has_permissions(ban_members=True)
    async def ban(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, reason: str = "Nothing"):

        if member == inter.author:
            await inter.response.send_message("You can`t ban yourself!", ephemeral=True)
            return
            
        if member == self.bot.user:
            await inter.response.send_message("I can`t ban myself!", ephemeral=True)
            return
        
        embed = disnake.Embed(color=colors.RED, title="Ban", description=f"User {member.mention} has been banned from {inter.guild} for reason: {reason}")
        logs_channel = self.bot.get_channel(1476247810985689139)

        await member.ban(reason=reason)
        
        await inter.response.send_message("Done!", ephemeral=True)
        await logs_channel.send(embed=embed)

    @ban.error
    async def ban_error(self, inter: disnake.ApplicationCommandInteraction, error):

        if isinstance(error, commands.MissingPermissions):
            await inter.response.send_message("You haven`t permissions!")

def setup(bot):
    bot.add_cog(BanCommand(bot))
