import disnake
from disnake.ext import commands

from utils import colors

class ReactionLog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):

        if user == self.bot.user:
            return

        embed = disnake.Embed(color=colors.BLUE, title="New Reaction", description=f"{user.mention} added reaction `{reaction}` on message \n```{reaction.message.content}``` \nID: {reaction.message.id}")
        logs_channel = self.bot.get_channel(1476247810985689139)

        await logs_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):

        if user == self.bot.user:
            return

        embed = disnake.Embed(color=colors.BLUE, title="Reaction Removed", description=f"{user.mention} removed reaction `{reaction}` on message \n```{reaction.message.content}``` \nID: {reaction.message.id}")
        logs_channel = self.bot.get_channel(1476247810985689139)

        await logs_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_reaction_clear(self, message, reactions):

        reaction: list = []

        for t in reactions:
            emoji = t.emoji
            reaction.append(emoji)

        embed = disnake.Embed(color=colors.BLUE, title="Reaction Clear", description=f"Reactions `{reaction}` has been cleared on message \n```{message.content}``` \nID: {message.id}")
        logs_channel = self.bot.get_channel(1476247810985689139)

        await logs_channel.send(embed=embed)

def setup(bot):
    bot.add_cog(ReactionLog(bot))
