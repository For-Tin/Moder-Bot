from disnake.ext import commands

class ReactionLog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):

        msg = f"{user.mention} add reaction {reaction} on message: {reaction.message.content} (ID: {reaction.message.id})"

        logs_channel = self.bot.get_channel(1476247810985689139)

        await logs_channel.send(msg)

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):

        msg = f"{user.mention} remove reaction {reaction} on message: {reaction.message.content} (ID: {reaction.message.id})"

        logs_channel = self.bot.get_channel(1476247810985689139)

        await logs_channel.send(msg)

def setup(bot):
    bot.add_cog(ReactionLog(bot))
