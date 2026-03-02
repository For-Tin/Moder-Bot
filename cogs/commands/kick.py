import disnake
from disnake.ext import commands

class KickCommand(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="kick", description="Kick member")
    @commands.has_permissions(kick_members=True)
    async def kick(self, inter, member: disnake.Member, reason: str = "Nothing"):

        if member == inter.author:
            await inter.response.send_message("You can`t kick yourself!")
            return
            
        if member == self.bot.user:
            await inter.response.send_message("I can`t kick myself!")
            return
        
        await member.kick(reason=reason)
        await inter.send(f"User {member.mention} has been kicked from {inter.guild} for reason: {reason}")

def setup(bot):
    bot.add_cog(KickCommand(bot))
