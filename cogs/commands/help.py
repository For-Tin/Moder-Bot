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
                        value="`/help` - ON")
        
        embed.add_field(name="Bank",
                        value="`/balance` - ON \n" \
                        "`/pay` - ON")
        
        embed.add_field(name="Mod",
                        value="`/kick` - ON \n" \
                        "`/ban` - ON \n" \
                        "`/unban` - DONT WORK!\n" \
                        "`/mute` - OFF")

        await inter.response.send_message(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(HelpCommand(bot))
