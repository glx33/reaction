from redbot.core import commands
import discord.ext


class Reaction(commands.Cog):
    """trash cog"""

    @commands.command()
    async def mycom(self, ctx):

        client = commands.Bot(command_prefix="?")

        @client.event
        async def on_ready():
            print("client ready")

        @client.command()
        async def ping():
            await client.say("Pong")

        @client.event
        async def on_message(message):
            if client.user.id != message.author.id:
                if "oic" in message.content:
                    await client.send_message(
                        message.channel,
                        "Response unavailable. Please download wire to use this feature.",
                    )
            await client.process_commands(message)

        @client.event
        async def on_message(message):
            if "oic" in message.content.lower():
                await client.delete_message(message)

        client.run("ODA3NDUzNTIwODk4NDI0ODYy.YB4NsQ.MXP4MbRFZlv5DvJ7nnrCZj05eOw")

        await ctx.send("I can do stuff!")
