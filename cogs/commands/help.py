import disnake
from disnake.ext import commands

from utils import colors

class HelpCommand(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="help", description="All commands")
    async def help(self, inter: disnake.ApplicationCommandInteraction):

        embed = disnake.Embed(color=colors.GREEN,
                              title="Help",
                              description="All commands")
        embed.add_field(name="Simple",
                        value="`/help` - On")
        embed.add_field(name="Mod",
                        value="`/kick` - On \n" \
                        "`/ban` - On \n" \
                        "`/unban` - Off \n" \
                        "`/mute` - Off")

        await inter.response.send_message(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(HelpCommand(bot))
