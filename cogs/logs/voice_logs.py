import disnake
from disnake.ext import commands

from utils import colors

class VoiceLog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):

        if after.channel is None:
            embed = disnake.Embed(color=colors.BLUE, title="Leaved Voice", description=f"{member.mention} disconnected from **{before.channel.name}** (ID: {before.channel.id})")
            logs_channel = self.bot.get_channel(1476247810985689139)
            await logs_channel.send(embed=embed)
        else:
            embed = disnake.Embed(color=colors.BLUE, title="Join Voice", description=f"{member.mention} connected to **{after.channel.name}** (ID: {after.channel.id})")
            logs_channel = self.bot.get_channel(1476247810985689139)
            await logs_channel.send(embed=embed)

def setup(bot):
    bot.add_cog(VoiceLog(bot))
