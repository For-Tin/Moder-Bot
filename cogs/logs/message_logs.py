from disnake.ext import commands

class MessageLog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.bot.user:
            return
        
        msg = f"New message from {message.author.mention}: {message.content} (ID: {message.id})"
        logs_channel = self.bot.get_channel(1476247810985689139)

        await logs_channel.send(msg)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):

        if before.content == after.content:
            return

        msg = f"Edit message from {before.author.mention}: {before.content} => {after.content} (ID: {after.id})"
        logs_channel = self.bot.get_channel(1476247810985689139)

        await logs_channel.send(msg)
    
    @commands.Cog.listener()
    async def on_message_delete(self, message):

        if message.author == self.bot.user:
            return
        
        msg = f"Message from {message.author.mention} has been deleted: {message.content} (with id {message.id})"
        logs_channel = self.bot.get_channel(1476247810985689139)

        await logs_channel.send(msg)

def setup(bot):
    bot.add_cog(MessageLog(bot))
