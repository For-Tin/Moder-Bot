import disnake
from disnake.ext import commands

class BanCommand(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="ban", description="Ban member")
    @commands.has_permissions(ban_members=True)
    async def ban(self, inter, member: disnake.Member, reason: str = "Nothing"):

        if member == inter.author:
            await inter.response.send_message("You can`t ban yourself!")
            return
            
        if member == self.bot.user:
            await inter.response.send_message("I can`t ban myself!")
            return
        
        await member.ban(reason=reason)
        await inter.send(f"User {member.mention} has been banned from {inter.guild} for reason: {reason}")

def setup(bot):
    bot.add_cog(BanCommand(bot))
