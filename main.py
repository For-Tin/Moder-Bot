import disnake
import os
from dotenv import load_dotenv

class Client(disnake.Client):
    async def on_ready(self):
        print(f'{self.user} -> Ready!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        msg = (f"New message from {message.author}: {message.content} (with id {message.id})")
        logs_channel = self.get_channel(int(os.getenv("LOGS_CHANNEL")))
        await logs_channel.send(msg)
    
    async def on_message_delete(self, message):
        msg = f"Message from {message.author} has been deleted: {message.content} (with id {message.id})"
        logs_channel = self.get_channel(int(os.getenv("LOGS_CHANNEL")))
        await logs_channel.send(msg)

    async def on_reaction_add(self, reaction, user):
        msg = f"{user} add reaction {reaction} on message: {reaction.message.content} (with id {reaction.message.id})"
        logs_channel = self.get_channel(int(os.getenv("LOGS_CHANNEL")))
        await logs_channel.send(msg)

    async def on_reaction_remove(self, reaction, user):
        msg = f"{user} remove reaction {reaction} on message: {reaction.message.content} (with id {reaction.message.id})"
        logs_channel = self.get_channel(int(os.getenv("LOGS_CHANNEL")))
        await logs_channel.send(msg)

if __name__ == "__main__":
    client = Client(intents=disnake.Intents.all())
    load_dotenv()
    client.run(os.getenv("TOKEN_BOT"))
