import disnake
from disnake.ext import commands

from utils import colors

class MessageLog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.bot.user:
            return
        
        embed = disnake.Embed(color=colors.BLUE, title="New Message", description=f"New message from {message.author.mention} \n```{message.content}``` \nID: {message.id}")
        logs_channel = self.bot.get_channel(1476247810985689139)

        await logs_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):

        if before.content == after.content:
            return

        embed = disnake.Embed(color=colors.BLUE, title="Message Edited", description=f"Message edited from {before.author.mention} \n**Before:** \n```{before.content}``` \n**After:** \n```{after.content}``` \nID: {after.id}")
        logs_channel = self.bot.get_channel(1476247810985689139)

        await logs_channel.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_message_delete(self, message):

        if message.author == self.bot.user:
            return
        
        embed = disnake.Embed(color=colors.BLUE, title="Message Delited", description=f"Message from {message.author.mention} has been deleted \n```{message.content}``` \nID: {message.id}")
        logs_channel = self.bot.get_channel(1476247810985689139)

        await logs_channel.send(embed=embed)

def setup(bot):
    bot.add_cog(MessageLog(bot))
