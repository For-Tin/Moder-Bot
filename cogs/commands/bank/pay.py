import disnake
from disnake.ext import commands

import supabase

from utils import colors

class PayCommand(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="pay", description="")
    async def pay(self, inter: disnake.ApplicationCommandInteraction, payee: disnake.Member, quantity: float):

        db: supabase.Client = self.bot.db
        sender_stat = db.table("users").select("discord_id, balance").eq("discord_id", inter.user.id).maybe_single().execute()
        payee_stat = db.table("users").select("discord_id, balance").eq("discord_id", payee.id).maybe_single().execute()

        if sender_stat is None:
            sender_stat = db.table("users").insert({"discord_id":inter.user.id, "name":inter.user.display_name, "username":inter.user.name}).execute()
            sender_stat.data = sender_stat.data[0]

        if payee_stat is None:
            payee_stat = db.table("users").insert({"discord_id":payee.id, "name":payee.display_name, "username":payee.name}).execute()
            payee_stat.data = payee_stat.data[0]

        sender_balance: float = sender_stat.data["balance"]
        payee_balance: float = payee_stat.data["balance"]

        embed = disnake.Embed(color=colors.BLUE, title="Pay", description=f"User {inter.user.mention} transferred **{quantity}₿** to {payee.mention}")
        logs_channel = self.bot.get_channel(1476247810985689139)

        if sender_balance >= quantity:
            sender_balance -= quantity
            payee_balance += quantity

            db.table("users").update({"balance": sender_balance}).eq("discord_id", inter.user.id).execute()
            db.table("users").update({"balance": payee_balance}).eq("discord_id", payee.id).execute()

            await inter.response.send_message("Done!", ephemeral=True)
            await logs_channel.send(embed=embed)
        else:
            await inter.response.send_message("Not enough money!", ephemeral=True)

def setup(bot):
    bot.add_cog(PayCommand(bot))
