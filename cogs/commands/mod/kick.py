import disnake
from disnake.ext import commands

from utils import colors

class KickCommand(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="kick", description="Kick member")
    @commands.has_permissions(kick_members=True)
    async def kick(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, reason: str = "Nothing"):

        if member == inter.author:
            await inter.response.send_message("You can`t kick yourself!", ephemeral=True)
            return
            
        if member == self.bot.user:
            await inter.response.send_message("I can`t kick myself!", ephemeral=True)
            return
        
        embed = disnake.Embed(color=colors.RED, title="Kick", description=f"User {member.mention} has been kicked from {inter.guild} for reason: \n`{reason}`")
        logs_channel = self.bot.get_channel(1476247810985689139)

        await member.kick(reason=reason)
        
        await inter.response.send_message("Done!", ephemeral=True)
        await logs_channel.send(embed=embed)

    @kick.error
    async def kick_error(self, inter: disnake.ApplicationCommandInteraction, error):

        if isinstance(error, commands.MissingPermissions):
            await inter.response.send_message("You haven`t permissions!")

def setup(bot):
    bot.add_cog(KickCommand(bot))
